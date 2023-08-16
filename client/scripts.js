const GPTResearcher = (() => {
    // ... existing code ...

    const writeReport = (data, converter) => {
      const reportContainer = document.getElementById("reportContainer");
      const markdownOutput = converter.makeHtml(data.output);
      reportContainer.innerHTML += markdownOutput;
      updateScroll();

      // Find all the Mermaid diagrams in the report container
      const mermaidDiagrams = reportContainer.querySelectorAll(".mermaid");

      // Render each Mermaid diagram
      mermaidDiagrams.forEach((diagram) => {
        mermaid.render(diagram.id, diagram.textContent, (svgCode) => {
          diagram.innerHTML = svgCode;
        });
      });

      // Convert Mermaid diagrams to SVG
      const mermaidElements = reportContainer.querySelectorAll(".mermaid");
      mermaidElements.forEach((element) => {
        const mermaidCode = element.textContent;
        const svgCode = mermaid.mermaidAPI.render("mermaid-svg-" + Math.random(), mermaidCode);
        element.innerHTML = svgCode;
      });
    };

    // ... existing code ...

    return {
      startResearch,
      copyToClipboard,
    };
})();
