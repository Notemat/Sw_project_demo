document.addEventListener('DOMContentLoaded', function () {
  // Получаем все ссылки в меню
  const menuLinks = document.querySelectorAll('.menu-link');


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
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: true, // Включены стрелки
    dots: false,  // Отключаем точки
    draggable: true, // Отключаем перетаскивание мышкой
    touchMove: true,
    responsive: [
      {
        breakpoint: 720,
        settings: {
          slidesToShow: 3,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 360,
        settings: {
          slidesToShow: 1,
        }
      }
    ]
  });

  // Функция для выравнивания высоты всех ячеек
  function setEqualHeight() {
    let maxHeight = 0;

    // Сбрасываем высоту, чтобы избежать наложения значений
    $('.carousel .slick-slide').css('height', 'auto');

    // Вычисляем максимальную высоту среди слайдов
    $('.carousel .slick-slide').each(function() {
      let thisHeight = $(this).outerHeight();
      if (thisHeight > maxHeight) {
        maxHeight = thisHeight;
      }
    });

    // Применяем максимальную высоту ко всем слайдам
    $('.carousel .slick-slide').css('height', maxHeight + 'px');
  }

  // Устанавливаем одинаковую высоту при загрузке
  setEqualHeight();

  // Устанавливаем одинаковую высоту при изменении размера окна
  $(window).on('resize', function() {
    setEqualHeight();
  });

  // Добавляем прокрутку колесом мыши
  $('.carousel').on('wheel', function(e) {
    e.preventDefault();

    if (e.originalEvent.deltaY < 0) {
      $(this).slick('slickPrev');
    } else {
      $(this).slick('slickNext');
    }
  });
});