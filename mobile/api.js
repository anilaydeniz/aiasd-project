// mobile/api.js
// KitchenOps mobile API client for server communication
export const SERVER = 'https://kitchenops-api-ekg4.onrender.com'; // Live 24/7 Render Cloud Server
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

