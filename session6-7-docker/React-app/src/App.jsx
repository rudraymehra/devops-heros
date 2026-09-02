const styles = {
  body: {
    margin: 0,
    fontFamily: 'Arial, sans-serif',
    background: '#0f2027',
    color: '#f9fafb',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
  },
  card: {
    background: '#1c3a47',
    padding: '40px 60px',
    borderRadius: '12px',
    textAlign: 'center',
    boxShadow: '0 8px 24px rgba(0,0,0,0.4)',
  },
  h1: { margin: '0 0 10px', color: '#61dafb' },
  p: { margin: 0, color: '#d1d5db' },
};

export default function App() {
  return (
    <div style={styles.body}>
      <div style={styles.card}>
        <h1 style={styles.h1}>Hello World from React!</h1>
        <p style={styles.p}>Built with Vite, served by Nginx inside a Docker container</p>
      </div>
    </div>
  );
}
