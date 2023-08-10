const selectableTags = document.querySelectorAll('.selectable-tag');
const copyAllLink = document.getElementById('copy-all-link');

selectableTags.forEach(tagButton => {
  tagButton.addEventListener('click', () => {
    const tag = tagButton.getAttribute('data-tag');
    copyToClipboard(tag);
  });
});

copyAllLink.addEventListener('click', () => {
  const allTags = Array.from(selectableTags).map(tagButton => tagButton.getAttribute('data-tag')).join(', ');
  copyToClipboard(allTags);
});

function copyToClipboard(text) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand('copy');
  document.body.removeChild(textarea);
  alert('Tag(s) copied to clipboard: ' + text);
}
