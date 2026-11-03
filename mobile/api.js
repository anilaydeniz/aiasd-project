// mobile/api.js
// KitchenOps mobile API client for server communication
export const SERVER = 'http://172.20.10.2:8000'; // Laptop IPv4 address on hotspot/Wi-Fi
let token = null;

export const setToken = (t) => {
  token = t;
};

export const getToken = () => token;

export async function api(method, path, body) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(SERVER + path, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const data = await response.json().catch(() => ({}));
    return { status: response.status, data };
  } catch (error) {
    return {
      status: 503,
      data: { detail: 'Cannot reach server at ' + SERVER + '. Check network connection.' },
    };
  }
}
