import React, {useEffect, useRef, useState} from 'react';
import {createRoot} from 'react-dom/client';
import './styles.css';

const categories = ['ELECTRICAL', 'PLUMBING', 'NETWORK', 'FURNITURE', 'OTHER'];
const labels = {REPORTED: 'Reported', IN_PROGRESS: 'In progress', RESOLVED: 'Resolved'};
const pretty = text => text.charAt(0) + text.slice(1).toLowerCase().replaceAll('_', ' ');
const emptyRequest = () => ({title: '', description: '', location: '', category: 'ELECTRICAL', urgency: 'NORMAL', reporter: 'Sudhir Mehra'});
const when = value => new Date(value.endsWith('Z') || value.includes('+') ? value : value + 'Z').toLocaleString([], {month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'});

async function api(path, method = 'GET', body) {
  const response = await fetch('/api' + path, {method, headers: {'Content-Type': 'application/json'}, ...(body ? {body: JSON.stringify(body)} : {})});
  if (!response.ok) {
    const payload = await response.json().catch(() => ({}));
    const detail = payload.detail;
    throw new Error(typeof detail === 'string' ? detail : Array.isArray(detail) ? detail.map(x => x.msg).join('; ') : 'Request failed. Please try again.');
  }
  return response.status === 204 ? null : response.json();
}

function Modal({title, children, close}) {
  const dialog = useRef(null);
  useEffect(() => {
    dialog.current.showModal();
    return () => dialog.current?.close();
  }, []);
  return <dialog ref={dialog} onCancel={close} aria-label={title}>
    <div className="modal-heading"><h2>{title}</h2><button className="icon-button" onClick={close} aria-label="Close dialog">×</button></div>
    {children}
  </dialog>;
}

function App() {
  const [requests, setRequests] = useState([]);
  const [activity, setActivity] = useState([]);
  const [stats, setStats] = useState({total: 0, reported: 0, inProgress: 0, resolved: 0, urgentOpen: 0});
  const [filter, setFilter] = useState('ALL');
  const [category, setCategory] = useState('ALL');
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');
  const [form, setForm] = useState(null);
  const [draft, setDraft] = useState(emptyRequest);
  const [selectedId, setSelectedId] = useState(null);
  const [resolution, setResolution] = useState('');
  const [deleteId, setDeleteId] = useState(null);
  const selected = requests.find(item => item.id === selectedId);

  async function load() {
    const [items, totals, events] = await Promise.all([api('/requests'), api('/requests/stats'), api('/activity')]);
    setRequests(items); setStats(totals); setActivity(events);
  }
  useEffect(() => {
    load().catch(e => setError(e.message)).finally(() => setLoading(false));
  }, []);
  async function perform(action, message, after = () => {}) {
    setBusy(true); setError(''); setNotice('');
    try { await action(); await load(); after(); setNotice(message); }
    catch (e) { setError(e.message); }
    finally { setBusy(false); }
  }
  function startForm(item) {
    setSelectedId(null); setError('');
    setForm(item ? item.id : 'new');
    setDraft(item ? {title: item.title, description: item.description, location: item.location, category: item.category, urgency: item.urgency, reporter: item.reporter} : emptyRequest());
  }
  function submit(event) {
    event.preventDefault();
    const payload = {...draft};
    if (form !== 'new') delete payload.reporter;
    perform(() => api(form === 'new' ? '/requests' : '/requests/' + form, form === 'new' ? 'POST' : 'PUT', payload), 'Request saved.', () => setForm(null));
  }
  function changeStatus(item, status, notes = '') {
    perform(() => api('/requests/' + item.id, 'PUT', {status, ...(status === 'RESOLVED' ? {resolution: notes} : {})}), 'Request updated.', () => {setSelectedId(null); setResolution('');});
  }
  const visible = requests.filter(item => (filter === 'ALL' || item.status === filter) && (category === 'ALL' || item.category === category) && (item.title + ' ' + item.location).toLowerCase().includes(search.toLowerCase().trim()));
  const errorView = error && <p role="alert" className="alert">{error}</p>;

  return <div className="workspace">
    <aside className="sidebar">
      <a href="#" className="brand" aria-label="CampusFix home"><span className="brand-icon">C<span>+</span></span><div>CampusFix<small>A better place to learn.</small></div></a>
      <p className="sidebar-label">CAMPUS OPERATIONS</p>
      <button className="nav-item active" onClick={() => {setFilter('ALL'); setSearch(''); setCategory('ALL');}}>▤ <span>Maintenance desk</span><b>{stats.total}</b></button>
      <div className="sidebar-note"><span className="note-symbol">↗</span><h3>Small fixes.<br/>Better campus.</h3><p>Report an issue, track the repair, and close the loop.</p></div>
      <div className="profile"><span className="avatar">SM</span><div><strong>Sudhir Mehra</strong><small>24 BCS 10425 · Batch B</small></div></div>
    </aside>
    <main>
      <header className="page-header"><div><p className="eyebrow">CAMPUS / MAINTENANCE</p><h1>Let’s get it fixed.</h1><p className="subtitle">One place for the things that need attention.</p></div><button className="primary" onClick={() => startForm(null)}>＋ Report an issue</button></header>
      {!form && !selected && !deleteId && errorView}
      {notice && <p className="notice" role="status">{notice}</p>}
      <section className="stats" aria-label="Request statistics">
        {[['Reported', stats.reported, 'Waiting for attention', 'reported'], ['In progress', stats.inProgress, 'Repairs underway', 'progress'], ['Resolved', stats.resolved, 'Back in working order', 'resolved'], ['Urgent & open', stats.urgentOpen, 'Needs priority attention', 'urgent']].map(([title, count, sub, color]) => <div className={'stat ' + color} key={title}><p>{title}<span className="stat-dot"/></p><strong>{count}</strong><small>{sub}</small></div>)}
      </section>
      <div className="desk-grid">
        <section className="request-panel">
          <div className="section-heading"><h2>Maintenance requests <span>{requests.length}</span></h2><button className="text-button" disabled={busy} onClick={() => perform(async () => {}, 'Desk refreshed.')}>↻ Refresh</button></div>
          <div className="filters" aria-label="Filter by status">{['ALL', 'REPORTED', 'IN_PROGRESS', 'RESOLVED'].map(value => <button key={value} className={filter === value ? 'selected' : ''} aria-pressed={filter === value} onClick={() => setFilter(value)}>{value === 'ALL' ? 'All requests' : labels[value]}</button>)}</div>
          <div className="search-row"><label className="search"><span className="sr-only">Search requests</span><input value={search} onChange={e => setSearch(e.target.value)} placeholder="Search an issue or location…"/></label><label><span className="sr-only">Category filter</span><select aria-label="Category filter" value={category} onChange={e => setCategory(e.target.value)}><option value="ALL">All categories</option>{categories.map(value => <option key={value} value={value}>{pretty(value)}</option>)}</select></label></div>
          {loading ? <p className="empty">Loading the maintenance desk…</p> : <div className="request-list">
            {visible.map(item => <article key={item.id} className="request-card">
              <div className={'category-icon ' + item.category.toLowerCase()} aria-hidden="true">{{ELECTRICAL: 'ϟ', PLUMBING: '◉', NETWORK: '⌁', FURNITURE: '▥', OTHER: '◇'}[item.category]}</div>
              <div className="request-content"><div className="request-meta"><span>CF-{String(item.id).padStart(4, '0')}</span><span>·</span><span>{pretty(item.category)}</span>{item.urgency === 'URGENT' && <span className="urgency">Urgent</span>}</div><button className="request-title" onClick={() => {setSelectedId(item.id); setResolution(''); setError('');}}>{item.title}</button><p className="location">⌖ {item.location}</p><p className="description">{item.description || 'No additional details.'}</p><div className="request-footer"><span>Reported by {item.reporter}</span><time dateTime={item.created_at}>{when(item.created_at)}</time></div></div>
              <span className={'status ' + item.status.toLowerCase()}>{labels[item.status]}</span>
            </article>)}
            {!visible.length && <div className="empty"><span>◇</span><h3>{requests.length ? 'No matching requests' : 'A clear desk. A fresh start.'}</h3><p>{requests.length ? 'Try another status, category, or search.' : 'Report the first maintenance issue to get started.'}</p></div>}
          </div>}
          <div className="list-footer">Showing {visible.length} of {requests.length} requests</div>
        </section>
        <aside className="right-column">
          <section className="activity-panel"><div className="section-heading"><h2>Recent activity</h2><span className="live-dot"/></div><p className="panel-caption">Updates from your maintenance desk</p>{activity.map(event => <div className="activity-item" key={event.id}><span className="event-dot"/><div><p>{event.message}</p><time dateTime={event.created_at}>{when(event.created_at)}</time></div></div>)}{!activity.length && <p className="empty-small">Activity appears after a request is reported or updated.</p>}</section>
          <section className="help-card"><span>THE REPAIR LOOP</span><h3>Every report<br/>has a next step.</h3><ol><li>Report the issue and location.</li><li>Start work when it’s picked up.</li><li>Resolve it with a repair note.</li></ol><p>Still broken? Reopen a resolved request.</p></section>
        </aside>
      </div>
      <footer className="page-footer"><span>CampusFix · Campus maintenance desk</span><span>Built by Sudhir Mehra</span></footer>
    </main>
    {form && <Modal title={form === 'new' ? 'Report a campus issue' : 'Edit request'} close={() => !busy && setForm(null)}><p className="modal-intro">A clear location and description help the repair reach the right place.</p>{errorView}<form onSubmit={submit}>
      <label>Issue title<input autoFocus required minLength={3} maxLength={200} value={draft.title} onChange={e => setDraft({...draft, title: e.target.value})} placeholder="e.g. Reading lamp flickers"/></label>
      <label>Location<input required minLength={2} maxLength={100} value={draft.location} onChange={e => setDraft({...draft, location: e.target.value})} placeholder="e.g. Library, second floor, desk 12"/></label>
      <div className="form-grid"><label>Category<select aria-label="Category" value={draft.category} onChange={e => setDraft({...draft, category: e.target.value})}>{categories.map(value => <option key={value} value={value}>{pretty(value)}</option>)}</select></label><label>Urgency<select aria-label="Urgency" value={draft.urgency} onChange={e => setDraft({...draft, urgency: e.target.value})}><option value="NORMAL">Normal</option><option value="URGENT">Urgent</option></select></label></div>
      <label>Description<textarea maxLength={4000} value={draft.description} onChange={e => setDraft({...draft, description: e.target.value})} placeholder="What is happening, and when did it start?"/></label>
      <label>Reported by<input required minLength={2} maxLength={120} disabled={form !== 'new'} value={draft.reporter} onChange={e => setDraft({...draft, reporter: e.target.value})}/></label>
      <button className="primary full" disabled={busy}>{busy ? 'Saving…' : 'Save request'}</button>
    </form></Modal>}
    {selected && <Modal title={'CF-' + String(selected.id).padStart(4, '0')} close={() => !busy && setSelectedId(null)}>{errorView}<h3 className="detail-title">{selected.title}</h3><p className="location">{selected.location} · {pretty(selected.category)}</p><span className={'status ' + selected.status.toLowerCase()}>{labels[selected.status]}</span><p className="detail-body">{selected.description || 'No description provided.'}</p>
      {selected.status === 'RESOLVED' && <div className="resolution-note"><strong>Resolution</strong><p>{selected.resolution}</p></div>}
      <div className="detail-actions"><button disabled={busy} onClick={() => startForm(selected)}>Edit details</button><button className="danger" disabled={busy} onClick={() => {setDeleteId(selected.id); setSelectedId(null);}}>Delete request</button></div>
      {selected.status === 'REPORTED' && <button className="primary full" disabled={busy} onClick={() => changeStatus(selected, 'IN_PROGRESS')}>Start work</button>}
      {selected.status === 'IN_PROGRESS' && <form onSubmit={e => {e.preventDefault(); changeStatus(selected, 'RESOLVED', resolution);}}><label>Resolution notes<textarea required maxLength={4000} value={resolution} onChange={e => setResolution(e.target.value)} placeholder="Describe the repair and how you verified it."/></label><button className="primary full" disabled={busy || !resolution.trim()}>Mark resolved</button></form>}
      {selected.status === 'RESOLVED' && <button className="primary full" disabled={busy} onClick={() => changeStatus(selected, 'REPORTED')}>Reopen request</button>}
    </Modal>}
    {deleteId && <Modal title="Delete this request?" close={() => !busy && setDeleteId(null)}>{errorView}<p>This removes the request and its activity history. This action cannot be undone.</p><div className="detail-actions"><button disabled={busy} onClick={() => setDeleteId(null)}>Keep request</button><button className="danger" disabled={busy} onClick={() => perform(() => api('/requests/' + deleteId, 'DELETE'), 'Request deleted.', () => setDeleteId(null))}>Delete permanently</button></div></Modal>}
  </div>;
}

createRoot(document.getElementById('root')).render(<App/>);
