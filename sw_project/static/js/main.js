document.addEventListener('DOMContentLoaded', function () {
  
  if (!window.location.pathname.includes('/grocery/')) {
  
    // Получаем все секции и ссылки в меню
    const sections = document.querySelectorAll("section");
    const menuLinks = document.querySelectorAll(".menu_link");

    // Функция для определения активной секции
    function setActiveSection() {
      let index = sections.length;

      // Определение активной секции в зависимости от скролла
      while (--index && window.scrollY + 100 < sections[index].offsetTop) {}

      // Убираем класс "active" со всех ссылок
      menuLinks.forEach(link => link.classList.remove("active"));

      // Назначаем класс "active" активной ссылке
      const activeLink = menuLinks[index];
      if (activeLink) {
        activeLink.classList.add("active");

        // Обновляем URL с якорем активной секции
        const sectionId = sections[index].id;
        if (history.pushState) {
            history.pushState(null, null, "#" + sectionId);
        } else {
            window.location.hash = "#" + sectionId;
        }
      }
    }
  }

  window.addEventListener("scroll", setActiveSection);

  let burger = document.querySelector('.burger-menu'),
    menu = document.querySelector('.bar_menu');

  burger.addEventListener('click', function(e) {
    menu.classList.toggle('open');
  });
});

function openWhatsAppChat() {
  window.open('https://wa.me/79182000207', '_blank');
}


AOS.init({
  offset: 200,
  duration: 600,
  once: true,
  easing: 'ease-in-out',
});