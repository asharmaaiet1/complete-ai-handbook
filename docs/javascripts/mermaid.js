document$.subscribe(() => {
  if (typeof mermaid !== "undefined") {
    mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: "neutral" });
    mermaid.run({ querySelector: ".mermaid" });
  }
});
