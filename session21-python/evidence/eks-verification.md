# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:48:04.878520+00:00

Working directory: .

```text
$ python3 session21-python/scripts/cloud-check.py
$ kubectl --context campusfix-eks --request-timeout=30s get nodes -o wide
NAME                                         STATUS   ROLES    AGE   VERSION               INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                        KERNEL-VERSION                     CONTAINER-RUNTIME
ip-10-20-1-116.ap-south-1.compute.internal   Ready    <none>   75m   v1.35.8-eks-3b4a6ca   10.20.1.116   <none>        Amazon Linux 2023.12.20260930   6.12.110-135.202.amzn2023.x86_64   containerd://2.2.7+unknown
ip-10-20-2-64.ap-south-1.compute.internal    Ready    <none>   75m   v1.35.8-eks-3b4a6ca   10.20.2.64    <none>        Amazon Linux 2023.12.20260930   6.12.110-135.202.amzn2023.x86_64   containerd://2.2.7+unknown
 
$ kubectl --context campusfix-eks --request-timeout=30s get pods,svc,pvc,hpa,ingress -n taskboard -o wide
NAME                                      READY   STATUS    RESTARTS   AGE   IP            NODE                                         NOMINATED NODE   READINESS GATES
pod/taskboard-backend-b6b57c5cf-9sn7x     1/1     Running   0          10m   10.20.1.224   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/taskboard-backend-b6b57c5cf-d26md     1/1     Running   0          10m   10.20.2.198   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/taskboard-frontend-66967b946f-69khs   1/1     Running   0          10m   10.20.1.60    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/taskboard-frontend-66967b946f-qpkbd   1/1     Running   0          10m   10.20.2.204   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/taskboard-postgres-5c4567ddcb-t87t2   1/1     Running   0          10m   10.20.2.229   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>

NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE   SELECTOR
service/backend              ClusterIP   172.20.80.124   <none>        8000/TCP   10m   app=taskboard-backend
service/taskboard-frontend   ClusterIP   172.20.99.131   <none>        80/TCP     10m   app=taskboard-frontend
service/taskboard-postgres   ClusterIP   172.20.211.51   <none>        5432/TCP   10m   app=taskboard-postgres

NAME                                            STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS    VOLUMEATTRIBUTESCLASS   AGE   VOLUMEMODE
persistentvolumeclaim/taskboard-postgres-data   Bound    pvc-2c1c6543-f3b2-45d2-91d4-eb3e1ee0a8ce   5Gi        RWO            campusfix-gp3   <unset>                 10m   Filesystem

NAME                                                    REFERENCE                      TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/taskboard-backend   Deployment/taskboard-backend   cpu: 2%/60%   2         6         2          10m

NAME                                  CLASS   HOSTS             ADDRESS         PORTS   AGE
ingress.networking.k8s.io/taskboard   nginx   campusfix.local   172.20.98.234   80      10m
 
/api/requests {"title": "Persistence verification", "description": "Synthetic report retained across database Pod replacement.", "location": "Cloud lab", "category": "OTHER", "urgency": "NORMAL", "reporter": "Sudhir Mehra", "id": 6, "status": "REPORTED", "resolution": "", "created_at": "2026-10-13T03:47:41.779678Z", "updated_at": "2026-10-13T03:47:41.779682Z"}
$ kubectl --context campusfix-eks --request-timeout=30s delete pod -n taskboard -l app=taskboard-postgres --wait=true
pod "taskboard-postgres-5c4567ddcb-t87t2" deleted from taskboard namespace
 
$ kubectl --context campusfix-eks --request-timeout=30s rollout status deployment/taskboard-postgres -n taskboard --timeout=180s
Waiting for deployment "taskboard-postgres" rollout to finish: 0 of 1 updated replicas are available...
deployment "taskboard-postgres" successfully rolled out
 
/api/requests/6 {"title": "Persistence verification", "description": "Synthetic report retained across database Pod replacement.", "location": "Cloud lab", "category": "OTHER", "urgency": "NORMAL", "reporter": "Sudhir Mehra", "id": 6, "status": "REPORTED", "resolution": "", "created_at": "2026-10-13T03:47:41.779678Z", "updated_at": "2026-10-13T03:47:41.779682Z"}
PASS: PostgreSQL PVC retains the exact report after database Pod replacement.
$ kubectl --context campusfix-eks --request-timeout=30s get pvc -n taskboard
NAME                      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS    VOLUMEATTRIBUTESCLASS   AGE
taskboard-postgres-data   Bound    pvc-2c1c6543-f3b2-45d2-91d4-eb3e1ee0a8ce   5Gi        RWO            campusfix-gp3   <unset>                 10m
 
$ kubectl --context campusfix-eks --request-timeout=30s get deployment/taskboard-backend -n taskboard -o jsonpath={.spec.template.spec.containers[0].readinessProbe} {.spec.template.spec.containers[0].livenessProbe}
{"failureThreshold":3,"httpGet":{"path":"/ready","port":8000,"scheme":"HTTP"},"initialDelaySeconds":10,"periodSeconds":10,"successThreshold":1,"timeoutSeconds":1} {"failureThreshold":3,"httpGet":{"path":"/health","port":8000,"scheme":"HTTP"},"initialDelaySeconds":20,"periodSeconds":15,"successThreshold":1,"timeoutSeconds":1} 
$ kubectl --context campusfix-eks --request-timeout=30s patch configmap taskboard-config -n taskboard --type=merge -p {"data": {"APP_NAME": "temporary-drift-test"}}
configmap/taskboard-config patched
 
$ kubectl --context campusfix-eks --request-timeout=30s annotate application campusfix -n argocd argocd.argoproj.io/refresh=hard --overwrite
application.argoproj.io/campusfix annotated
 
$ kubectl --context campusfix-eks --request-timeout=30s get configmap taskboard-config -n taskboard -o json
{
    "apiVersion": "v1",
    "data": {
        "APP_NAME": "CampusFix API",
        "ENVIRONMENT": "development"
    },
    "kind": "ConfigMap",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:/ConfigMap:taskboard/taskboard-config",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"data\":{\"APP_NAME\":\"CampusFix API\",\"ENVIRONMENT\":\"development\"},\"kind\":\"ConfigMap\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:/ConfigMap:taskboard/taskboard-config\"},\"name\":\"taskboard-config\",\"namespace\":\"taskboard\"}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-config",
        "namespace": "taskboard",
        "resourceVersion": "20377",
        "uid": "a67fc55f-c586-4d80-99eb-a812ca9670cb"
    }
}
 
PASS: Argo CD restored the committed application name after an intentional live edit.
$ kubectl --context campusfix-eks --request-timeout=30s get application campusfix -n argocd
NAME        SYNC STATUS   HEALTH STATUS
campusfix   Synced        Healthy
 
$ kubectl --context campusfix-eks --request-timeout=30s get pods -n monitoring
NAME                                             READY   STATUS    RESTARTS   AGE
kube-prometheus-stack-grafana-6cbcbb9d4c-w287h   3/3     Running   0          30m
kube-prometheus-stack-operator-fdf784bc5-htvk9   1/1     Running   0          30m
prometheus-kube-prometheus-stack-prometheus-0    2/2     Running   0          30m
 
PASS: backend Prometheus targets: [
  {
    "discoveredLabels": {
      "__address__": "10.20.1.224:8000",
      "__always_scrape_classic_histograms__": "false",
      "__convert_classic_histograms_to_nhcb__": "false",
      "__meta_kubernetes_endpoint_address_target_kind": "Pod",
      "__meta_kubernetes_endpoint_address_target_name": "taskboard-backend-b6b57c5cf-9sn7x",
      "__meta_kubernetes_endpoint_node_name": "ip-10-20-1-116.ap-south-1.compute.internal",
      "__meta_kubernetes_endpoint_port_name": "http",
      "__meta_kubernetes_endpoint_port_protocol": "TCP",
      "__meta_kubernetes_endpoint_ready": "true",
      "__meta_kubernetes_endpoints_annotation_endpoints_kubernetes_io_last_change_trigger_time": "2026-10-13T03:39:54Z",
      "__meta_kubernetes_endpoints_annotationpresent_endpoints_kubernetes_io_last_change_trigger_time": "true",
      "__meta_kubernetes_endpoints_label_app": "taskboard-backend",
      "__meta_kubernetes_endpoints_label_app_kubernetes_io_managed_by": "Helm",
      "__meta_kubernetes_endpoints_label_endpoints_kubernetes_io_managed_by": "endpoint-controller",
      "__meta_kubernetes_endpoints_labelpresent_app": "true",
      "__meta_kubernetes_endpoints_labelpresent_app_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_endpoints_labelpresent_endpoints_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_endpoints_name": "backend",
      "__meta_kubernetes_namespace": "taskboard",
      "__meta_kubernetes_pod_container_image": "ghcr.io/rudraymehra/campusfix-backend:0a1c12a5cbb3bb649b77f1be3b515357eca0d30e",
      "__meta_kubernetes_pod_container_init": "false",
      "__meta_kubernetes_pod_container_name": "backend",
      "__meta_kubernetes_pod_container_port_number": "8000",
      "__meta_kubernetes_pod_container_port_protocol": "TCP",
      "__meta_kubernetes_pod_controller_kind": "ReplicaSet",
      "__meta_kubernetes_pod_controller_name": "taskboard-backend-b6b57c5cf",
      "__meta_kubernetes_pod_host_ip": "10.20.1.116",
      "__meta_kubernetes_pod_ip": "10.20.1.224",
      "__meta_kubernetes_pod_label_app": "taskboard-backend",
      "__meta_kubernetes_pod_label_pod_template_hash": "b6b57c5cf",
      "__meta_kubernetes_pod_label_topology_kubernetes_io_region": "ap-south-1",
      "__meta_kubernetes_pod_label_topology_kubernetes_io_zone": "ap-south-1a",
      "__meta_kubernetes_pod_labelpresent_app": "true",
      "__meta_kubernetes_pod_labelpresent_pod_template_hash": "true",
      "__meta_kubernetes_pod_labelpresent_topology_kubernetes_io_region": "true",
      "__meta_kubernetes_pod_labelpresent_topology_kubernetes_io_zone": "true",
      "__meta_kubernetes_pod_name": "taskboard-backend-b6b57c5cf-9sn7x",
      "__meta_kubernetes_pod_node_name": "ip-10-20-1-116.ap-south-1.compute.internal",
      "__meta_kubernetes_pod_phase": "Running",
      "__meta_kubernetes_pod_ready": "true",
      "__meta_kubernetes_pod_uid": "b906f873-a6c9-4681-bf5e-9da600550fc0",
      "__meta_kubernetes_service_annotation_argocd_argoproj_io_tracking_id": "campusfix:/Service:taskboard/backend",
      "__meta_kubernetes_service_annotation_kubectl_kubernetes_io_last_applied_configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:/Service:taskboard/backend\"},\"labels\":{\"app\":\"taskboard-backend\"},\"name\":\"backend\",\"namespace\":\"taskboard\"},\"spec\":{\"ports\":[{\"name\":\"http\",\"port\":8000,\"targetPort\":8000}],\"selector\":{\"app\":\"taskboard-backend\"}}}\n",
      "__meta_kubernetes_service_annotation_meta_helm_sh_release_name": "taskboard",
      "__meta_kubernetes_service_annotation_meta_helm_sh_release_namespace": "taskboard",
      "__meta_kubernetes_service_annotationpresent_argocd_argoproj_io_tracking_id": "true",
      "__meta_kubernetes_service_annotationpresent_kubectl_kubernetes_io_last_applied_configuration": "true",
      "__meta_kubernetes_service_annotationpresent_meta_helm_sh_release_name": "true",
      "__meta_kubernetes_service_annotationpresent_meta_helm_sh_release_namespace": "true",
      "__meta_kubernetes_service_label_app": "taskboard-backend",
      "__meta_kubernetes_service_label_app_kubernetes_io_managed_by": "Helm",
      "__meta_kubernetes_service_labelpresent_app": "true",
      "__meta_kubernetes_service_labelpresent_app_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_service_name": "backend",
      "__metrics_path__": "/metrics",
      "__scheme__": "http",
      "__scrape_interval__": "15s",
      "__scrape_native_histograms__": "false",
      "__scrape_timeout__": "10s",
      "job": "serviceMonitor/taskboard/taskboard-backend/0"
    },
    "labels": {
      "container": "backend",
      "endpoint": "http",
      "instance": "10.20.1.224:8000",
      "job": "backend",
      "namespace": "taskboard",
      "pod": "taskboard-backend-b6b57c5cf-9sn7x",
      "service": "backend"
    },
    "scrapePool": "serviceMonitor/taskboard/taskboard-backend/0",
    "scrapeUrl": "http://10.20.1.224:8000/metrics",
    "globalUrl": "http://10.20.1.224:8000/metrics",
    "lastError": "",
    "lastScrape": "2026-10-13T03:48:00.573603192Z",
    "lastScrapeDuration": 0.191925633,
    "health": "up",
    "scrapeInterval": "15s",
    "scrapeTimeout": "10s"
  },
  {
    "discoveredLabels": {
      "__address__": "10.20.2.198:8000",
      "__always_scrape_classic_histograms__": "false",
      "__convert_classic_histograms_to_nhcb__": "false",
      "__meta_kubernetes_endpoint_address_target_kind": "Pod",
      "__meta_kubernetes_endpoint_address_target_name": "taskboard-backend-b6b57c5cf-d26md",
      "__meta_kubernetes_endpoint_node_name": "ip-10-20-2-64.ap-south-1.compute.internal",
      "__meta_kubernetes_endpoint_port_name": "http",
      "__meta_kubernetes_endpoint_port_protocol": "TCP",
      "__meta_kubernetes_endpoint_ready": "true",
      "__meta_kubernetes_endpoints_annotation_endpoints_kubernetes_io_last_change_trigger_time": "2026-10-13T03:39:54Z",
      "__meta_kubernetes_endpoints_annotationpresent_endpoints_kubernetes_io_last_change_trigger_time": "true",
      "__meta_kubernetes_endpoints_label_app": "taskboard-backend",
      "__meta_kubernetes_endpoints_label_app_kubernetes_io_managed_by": "Helm",
      "__meta_kubernetes_endpoints_label_endpoints_kubernetes_io_managed_by": "endpoint-controller",
      "__meta_kubernetes_endpoints_labelpresent_app": "true",
      "__meta_kubernetes_endpoints_labelpresent_app_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_endpoints_labelpresent_endpoints_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_endpoints_name": "backend",
      "__meta_kubernetes_namespace": "taskboard",
      "__meta_kubernetes_pod_container_image": "ghcr.io/rudraymehra/campusfix-backend:0a1c12a5cbb3bb649b77f1be3b515357eca0d30e",
      "__meta_kubernetes_pod_container_init": "false",
      "__meta_kubernetes_pod_container_name": "backend",
      "__meta_kubernetes_pod_container_port_number": "8000",
      "__meta_kubernetes_pod_container_port_protocol": "TCP",
      "__meta_kubernetes_pod_controller_kind": "ReplicaSet",
      "__meta_kubernetes_pod_controller_name": "taskboard-backend-b6b57c5cf",
      "__meta_kubernetes_pod_host_ip": "10.20.2.64",
      "__meta_kubernetes_pod_ip": "10.20.2.198",
      "__meta_kubernetes_pod_label_app": "taskboard-backend",
      "__meta_kubernetes_pod_label_pod_template_hash": "b6b57c5cf",
      "__meta_kubernetes_pod_label_topology_kubernetes_io_region": "ap-south-1",
      "__meta_kubernetes_pod_label_topology_kubernetes_io_zone": "ap-south-1b",
      "__meta_kubernetes_pod_labelpresent_app": "true",
      "__meta_kubernetes_pod_labelpresent_pod_template_hash": "true",
      "__meta_kubernetes_pod_labelpresent_topology_kubernetes_io_region": "true",
      "__meta_kubernetes_pod_labelpresent_topology_kubernetes_io_zone": "true",
      "__meta_kubernetes_pod_name": "taskboard-backend-b6b57c5cf-d26md",
      "__meta_kubernetes_pod_node_name": "ip-10-20-2-64.ap-south-1.compute.internal",
      "__meta_kubernetes_pod_phase": "Running",
      "__meta_kubernetes_pod_ready": "true",
      "__meta_kubernetes_pod_uid": "3ced0c4c-012f-47b8-a01b-282587dba791",
      "__meta_kubernetes_service_annotation_argocd_argoproj_io_tracking_id": "campusfix:/Service:taskboard/backend",
      "__meta_kubernetes_service_annotation_kubectl_kubernetes_io_last_applied_configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Service\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:/Service:taskboard/backend\"},\"labels\":{\"app\":\"taskboard-backend\"},\"name\":\"backend\",\"namespace\":\"taskboard\"},\"spec\":{\"ports\":[{\"name\":\"http\",\"port\":8000,\"targetPort\":8000}],\"selector\":{\"app\":\"taskboard-backend\"}}}\n",
      "__meta_kubernetes_service_annotation_meta_helm_sh_release_name": "taskboard",
      "__meta_kubernetes_service_annotation_meta_helm_sh_release_namespace": "taskboard",
      "__meta_kubernetes_service_annotationpresent_argocd_argoproj_io_tracking_id": "true",
      "__meta_kubernetes_service_annotationpresent_kubectl_kubernetes_io_last_applied_configuration": "true",
      "__meta_kubernetes_service_annotationpresent_meta_helm_sh_release_name": "true",
      "__meta_kubernetes_service_annotationpresent_meta_helm_sh_release_namespace": "true",
      "__meta_kubernetes_service_label_app": "taskboard-backend",
      "__meta_kubernetes_service_label_app_kubernetes_io_managed_by": "Helm",
      "__meta_kubernetes_service_labelpresent_app": "true",
      "__meta_kubernetes_service_labelpresent_app_kubernetes_io_managed_by": "true",
      "__meta_kubernetes_service_name": "backend",
      "__metrics_path__": "/metrics",
      "__scheme__": "http",
      "__scrape_interval__": "15s",
      "__scrape_native_histograms__": "false",
      "__scrape_timeout__": "10s",
      "job": "serviceMonitor/taskboard/taskboard-backend/0"
    },
    "labels": {
      "container": "backend",
      "endpoint": "http",
      "instance": "10.20.2.198:8000",
      "job": "backend",
      "namespace": "taskboard",
      "pod": "taskboard-backend-b6b57c5cf-d26md",
      "service": "backend"
    },
    "scrapePool": "serviceMonitor/taskboard/taskboard-backend/0",
    "scrapeUrl": "http://10.20.2.198:8000/metrics",
    "globalUrl": "http://10.20.2.198:8000/metrics",
    "lastError": "",
    "lastScrape": "2026-10-13T03:47:50.742701296Z",
    "lastScrapeDuration": 0.005560369,
    "health": "up",
    "scrapeInterval": "15s",
    "scrapeTimeout": "10s"
  }
]

```

Exit code: 0
