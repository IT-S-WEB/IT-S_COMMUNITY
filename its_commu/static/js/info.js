document.addEventListener("DOMContentLoaded", function() {
  const toggleBtns = document.querySelectorAll('.bi-chevron-right');
  const sidemenuItems = document.querySelectorAll('.sidemenu-item');

  //사이드메뉴 토글 클릭 시
  toggleBtns.forEach(function(toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      const sidemenuItemContent = toggleBtn.parentElement.nextElementSibling;
      const isVisible = sidemenuItemContent.classList.toggle('visible');

      //아이콘 변경
      toggleBtn.classList.toggle('bi-chevron-right', !isVisible);
      toggleBtn.classList.toggle('bi-chevron-down', isVisible);
    });
  });

  sidemenuItems.forEach(function(item) {
    item.addEventListener('click', function() {
      const contentType = item.getAttribute('data-content');
      loadContent(contentType);
    });
  });

  loadContent('info_its');
});


function loadContent(type) {
  let url = '';

  if (type === 'info_its') {
    url = '/details/info_its/';
  } else if (type === 'info_year') {
    url = '/details/info_year/';
  }

  fetch(url)
    .then(response => response.json())
    .then(data => {
      document.getElementById('content-area').innerHTML = data.html;
    })
    .catch(error => console.error('Error loading content:', error));
}