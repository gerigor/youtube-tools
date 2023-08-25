const copyButton = document.querySelector('.selectable-link');
const copyLink = document.querySelector('#copy-link');

copyButton.addEventListener('click', () => {
    const buttonText = copyButton.getAttribute('data-tag');
    copyToClipboard(buttonText);
});

copyLink.addEventListener('click', () => {
  const link =  copyButton.getAttribute('data-tag');
  copyToClipboard(link);
});

function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Link copied to clipboard: ' + text);
}