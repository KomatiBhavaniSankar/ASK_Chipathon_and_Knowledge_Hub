const providerEl = document.getElementById("provider");
const modelEl = document.getElementById("model");
const apiKeyWrapEl = document.getElementById("apiKeyWrap");
const apiKeyEl = document.getElementById("apiKey");
const kEl = document.getElementById("k");
const questionEl = document.getElementById("question");
const outputEl = document.getElementById("output");
const askBtn = document.getElementById("askBtn");
const clearBtn = document.getElementById("clearBtn");
const themeToggle = document.getElementById("themeToggle");

function syncProviderUI() {
  const provider = providerEl.value;

  if (provider === "groq") {
    apiKeyWrapEl.classList.remove("hidden");
    apiKeyEl.placeholder = "Enter your Groq API key";
    if (!modelEl.value || modelEl.value === "llama3") {
      modelEl.value = "llama-3.3-70b-versatile";
    }
  } else {
    apiKeyWrapEl.classList.add("hidden");
    if (!modelEl.value || modelEl.value === "llama-3.3-70b-versatile") {
      modelEl.value = "llama3";
    }
  }
}

providerEl.addEventListener("change", syncProviderUI);

askBtn.addEventListener("click", async () => {
  const provider = providerEl.value;
  const model = modelEl.value.trim();
  const apiKey = apiKeyEl.value.trim();
  const question = questionEl.value.trim();
  const k = parseInt(kEl.value || "4", 10);

  if (!question) {
    outputEl.textContent = "Please enter a question.";
    return;
  }

  if (provider === "groq" && !apiKey) {
    outputEl.textContent = "Please enter your Groq API key.";
    return;
  }

  outputEl.textContent = "Loading...";

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question,
        k,
        provider,
        model,
        api_key: apiKey || null
      })
    });

    let data;
    try {
      data = await res.json();
    } catch {
      data = null;
    }

    if (!res.ok) {
      outputEl.textContent =
        (data && (data.error || data.detail)) ||
        `Request failed with status ${res.status}`;
      return;
    }

    outputEl.textContent =
      (data && data.answer) ?? JSON.stringify(data, null, 2);
  } catch (err) {
    outputEl.textContent = "Request failed: " + err.message;
  }
});

clearBtn.addEventListener("click", () => {
  questionEl.value = "";
  outputEl.textContent = "Waiting for your question...";
});

themeToggle.addEventListener("click", () => {
  const html = document.documentElement;
  const current = html.getAttribute("data-theme") || "light";
  html.setAttribute("data-theme", current === "light" ? "dark" : "light");
});

syncProviderUI();