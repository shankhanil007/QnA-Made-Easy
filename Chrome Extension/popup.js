function myFunction() {
  fetch(`http://localhost:8000/speech`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((response) => response.json())
    .then((json) => {
      const text = json.text;
      document.getElementById("content").value = text;
    });
}

// Update the relevant fields with the new data.
const setDOMInfo = (info) => {
  meetid = info.id;
  document.getElementById("id").textContent = info.id;
  document.getElementById("myForm").action =
    "http://localhost:8000/" + meetid + "/postMessage";
};

window.addEventListener("DOMContentLoaded", () => {
  chrome.tabs.query(
    {
      active: true,
      currentWindow: true,
    },
    (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, {
        from: "popup",
        subject: "DOMInfo",
      });
    }
  );
});
