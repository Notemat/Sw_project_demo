document.addEventListener('DOMContentLoaded', function () {
  // Получаем все секции и ссылки в меню
  const sections = document.querySelectorAll("section");
  const menuLinks = document.querySelectorAll(".menu-link");
  const burger = document.querySelector('.burger-menu');
  const menu = document.querySelector('.bar-menu');
  const logo = document.querySelector('.logo-nav a');

  // Проверяем, находится ли пользователь на странице продуктов
  const isProductPage = window.location.pathname.includes('/grocery/');
  const isPrivacyPage = window.location.pathname.includes('/privacy-policy/');

  // Функция для определения активной секции
  function setActiveSection() {
    if (isProductPage) {
      // Если это страница продуктов, фиксируем вкладку "Продукция" как активную
      menuLinks.forEach(link => {
        if (link.textContent.trim() === 'Продукция') {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
      return; // Выходим из функции, так как скроллинг не должен менять активную вкладку
    }
    if (isPrivacyPage) {
      // Если это страница конфиденциальности, фиксируем вкладку "О нас" как активную
      menuLinks.forEach(link => {
        if (link.textContent.trim() === 'О нас') {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      });
      return; // Выходим из функции, так как скроллинг не должен менять активную вкладку
    }
  
  // Функция для определения активной секции
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

  // Обработчик клика по логотипу для мобильных устройств
  logo.addEventListener('click', function(event) {
    if (window.innerWidth <= 768) {
      event.preventDefault(); 
      menu.classList.toggle('open'); 
    }
  });

  // Открытие меню при клике на логотип (для промежуточной ширины)
  logo.addEventListener('click', function (e) {
    if (window.innerWidth < 1360 && window.innerWidth >= 768) {
      e.preventDefault(); 
      menu.classList.toggle('open');
    }
  });

  // Закрываем меню при клике за его пределами
  document.addEventListener('click', function(e) {
    if (!menu.contains(e.target) && !logo.contains(e.target) && menu.classList.contains('open')) {
      menu.classList.remove('open');
    }
  });

  // Добавляем обработчик клика для бургер-меню
  burger.addEventListener('click', function() {
    menu.classList.toggle('open');
  });

  // Добавляем обработчик прокрутки для активной секции
  window.addEventListener("scroll", setActiveSection);

  // Для десктопа логотип ведет на секцию home
  if (window.innerWidth > 1360) {
    logo.addEventListener('click', function() {
      window.location.href = "#home";
    });
  }
});

AOS.init({
  offset: 200,
  duration: 600,
  once: true,
  easing: 'ease-in-out',
});

function openWhatsAppChat() {
  const phoneNumber = "79990000000";
  const url = `https://wa.me/${phoneNumber}`;
  window.open(url, "_blank");
}

document.getElementById("whatsappButton").addEventListener("click", openWhatsAppChat);