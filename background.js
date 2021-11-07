chrome.runtime.onMessage.addListener((msg, sender) => {
  if (msg.subject === "showPageAction") {
    chrome.pageAction.show(sender.tab.id);
  }
});
