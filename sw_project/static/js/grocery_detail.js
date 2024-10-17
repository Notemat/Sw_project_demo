document.addEventListener('DOMContentLoaded', function () {
  // Получаем все ссылки в меню
  const menuLinks = document.querySelectorAll('.menu_link');

  // Проверяем наличие маршрута /grocery/ в URL
  if (window.location.pathname.includes('/grocery/')) {
    menuLinks.forEach(link => {
      // Делаем активной только кнопку "Продукты"
      if (link.textContent.trim() === 'Продукция') {
        link.classList.add('active');  // Добавляем класс active для кнопки Продукты
      } else {
        link.classList.remove('active');  // Убираем класс active с других ссылок
      }
    });
  }

  var modal = document.getElementById('modal');
  var btn = document.getElementById('btn-certificate');
  var span = document.querySelector('.close');

  // Открытие модального окна при клике на кнопку
  btn.onclick = function() {
    modal.style.display = 'block';
  }

  // Закрытие модального окна при клике на крестик
  span.onclick = function() {
    modal.style.display = 'none';
  }

  // Закрытие модального окна при клике вне области окна
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = 'none';
    }
  }
});
$(document).ready(function(){
  $('.carousel').slick({
    infinite: true,
    slidesToShow: 4,  // Количество элементов, отображаемых одновременно
    slidesToScroll: 1,
    arrows: true,  // Стрелки для прокрутки
    dots: true,    // Навигационные точки внизу
    responsive: [
      {
        breakpoint: 720,
        settings: {
          slidesToShow: 3
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 360,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  });
});
