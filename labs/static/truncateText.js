document.addEventListener('DOMContentLoaded', function() {
    // JavaScript function to truncate text
    function truncateText(element, maxLength) {
      var truncated = element.innerText;

      if (truncated.length > maxLength) {
        truncated = truncated.substr(0, maxLength) + '...';
      }

      return truncated;
    }


    var contentParagraphs = document.querySelectorAll('.p-6 #truncatedContent');

    var maxLength = 100; 

    contentParagraphs.forEach(function(contentParagraph) {
      contentParagraph.innerText = truncateText(contentParagraph, maxLength);
    });
  });