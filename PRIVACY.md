# Privacy Policy for KitchenOps

**Effective Date:** November 21, 2026  
**Application:** KitchenOps (Commercial Kitchen Inventory & Restock Logistics)  
**Developer:** Anıl Aydeniz (`220504045@st.atlas.edu.tr`)  
**Package Name:** `com.anilaydeniz.kitchenops`

---

## 1. Overview
KitchenOps is a commercial kitchen operations platform engineered for restaurant line chefs, kitchen managers, and purchasing staff. This Privacy Policy details how KitchenOps collects, processes, and protects your information across the FastAPI server, web management client, and React Native mobile application.

---

## 2. Information We Collect and Process

### 2.1 Authentication & Profile Data
* **E-mail Address:** We collect your professional or institutional e-mail address solely for passwordless authentication (REQ-001). A temporary 4-digit verification code (OTP) is dispatched to verify your identity.
* **Session Tokens:** Cryptographically signed Bearer session tokens are stored locally on your device to maintain secure sessions. We never store plain passwords.

### 2.2 Operational Kitchen Data
* **Inventory & Prep Records:** Ingredient stock counts, recipe formulations, dish preparation portions, and stock depletion audit logs (REQ-002).
* **Restock Logistics:** Ingredient safety thresholds, automated replenishment calculations, and supplier purchase orders (REQ-003).
* **Local Persistence:** Operational state is persistently stored in `server/data/kitchenops_db.json` on the server host to preserve pantry records across server restarts.

---

## 3. AI Kitchen Assistant & Third-Party LLM Processing (§5.4)

KitchenOps integrates an intelligent conversational assistant (REQ-009) to answer kitchen inquiries regarding stock levels, low-stock alerts, and recipe formulations.

### 3.1 Third-Party LLM Provider
* **Provider:** **Google Gemini API** (provided by Google LLC).
* **Service:** Google Generative AI REST API (`gemini-1.5-flash`).

### 3.2 Data Transmitted to the LLM API
* When you submit a question in the mobile Chat screen, the text of your query along with relevant non-sensitive kitchen context (current ingredient stock amounts, recipes, and items below safety threshold) is transmitted to the **Google Gemini API** over encrypted TLS (HTTPS).
* **Strict Privacy Isolation:** Personal identifiers, email addresses, passwords, and authorization tokens are **never** forwarded to the LLM API. The assistant only evaluates operational kitchen variables.
* **Usage Quota:** To prevent abusive resource consumption and maintain fair operational access, each authenticated user is capped at twenty (20) messages per calendar day.

---

## 4. Data Sharing and Third-Party Services
KitchenOps does not sell, lease, or monetize your operational or personal data. Data is exclusively shared with:
1. **Google LLC (Google Gemini API):** For processing interactive AI kitchen assistant requests as detailed above.
2. **Wholesale Food Suppliers:** Itemized purchase orders (ingredient name, reorder amount, supplier) dispatched upon explicit manager confirmation (REQ-003).

---

## 5. Security and Data Retention
* All client-server communications require authenticated HTTPS/TLS requests with Bearer tokens.
* Internal API keys (including `LLM_API_KEY`) reside exclusively in server-side environment variables and are never committed or exposed to client devices.
* Kitchen logs and purchase orders are retained for operational auditing and stock reconciliation purposes.

---

## 6. Contact Information
For privacy inquiries, data access requests, or bug reports regarding KitchenOps, please contact:
* **Lead Developer:** Anıl Aydeniz
* **Student ID:** 220504045
* **Contact E-mail:** `220504045@st.atlas.edu.tr`
* **Department:** Software Engineering, Atlas University
