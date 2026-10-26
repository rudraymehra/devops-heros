# Session 12 screenshots

## ConfigMap environment and volume injection

The terminal capture shows the ConfigMap applied, both consumer Pods Ready, environment keys visible in the environment-injection Pod, and mounted ConfigMap values read by the volume-injection Pod.

- [01-configmap-env-and-volume-injection.png](rudray-20261024-065559/01-configmap-env-and-volume-injection.png)

## Secret creation and Pod injection

The terminal capture shows the ConfigMap file values, a three-key Opaque Secret summarized by key sizes only, a successful backend rollout, and a check that the password environment variable exists with its value redacted.

- [01-configmap-files-and-secret-injection.png](rudray-20261024-065840/01-configmap-files-and-secret-injection.png)

## Ingress controller

The Minikube NGINX Ingress addon is enabled; the controller Pod is Ready and the controller Service exposes HTTP and HTTPS NodePorts. The HTTP and HTTPS host/path response checks below also passed.

- [01-ingress-addon-ready.png](rudray-20261024-142752/01-ingress-addon-ready.png)

## HTTP Ingress path routing

Both host-routed HTTP requests returned `200 OK`: `/` served the NGINX frontend and `/api/` served backend configuration values (no password).

- [01-http-ingress-path-routing.png](rudray-20261024-143112/01-http-ingress-path-routing.png)

## HTTPS Ingress host routing

Both TLS hosts returned `HTTP/2 200`: `portal.campus.local` served the frontend and `api.campus.local/api/` served the backend configuration. The lab uses a self-signed certificate, so curl used `-k`; no password was exposed.

- [01-https-ingress-host-routing.png](rudray-20261024-143450/01-https-ingress-host-routing.png)


## Secret newline bug and final resource inventory

The disposable `lab-demo` comparison shows the incorrect encoding decodes with a trailing `0a`, while the corrected value has no newline. The final inventory lists the Ingresses, ConfigMaps, Secrets (metadata only), Pods, and Services without exposing Secret data.

- [01-newline-bug-and-resource-inventory.png](rudray-20261024-143917/01-newline-bug-and-resource-inventory.png)
