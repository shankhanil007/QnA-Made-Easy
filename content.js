chrome.runtime.onMessage.addListener((msg, sender, response) => {
  if (msg.from === "popup" && msg.subject === "DOMInfo") {
    var domInfo = {
      id: document.querySelector(".Jyj1Td.CkXZgc").innerHTML,
    };
    response(domInfo);
  }
});
