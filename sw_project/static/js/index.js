$(document).ready(function () {
  let isDragging = false;
  let startX = 0;
  const dragThreshold = 15;

  // Инициализация карусели
  $('.element-list').slick({
    infinite: false,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
    draggable: true,
    touchMove: true,
    responsive: [
      { breakpoint: 1200, settings: { slidesToShow: 3 } },
      { breakpoint: 768, settings: { slidesToShow: 1 } },
      { breakpoint: 360, settings: { slidesToShow: 1 } },
    ],
  });

  // Отслеживаем начало перетаскивания
  $('.element-item').on('mousedown', function (e) {
    isDragging = false;
    startX = e.pageX;
  });

  // Отслеживаем движение мыши (перетаскивание)
  $('.element-item').on('mousemove', function (e) {
    if (Math.abs(e.pageX - startX) > dragThreshold) {
      isDragging = true;
    }
  });

  $('.element-item').on('mouseup', function (e) {
    if (isDragging) { // Если было перетаскивание, отменяем действие
        isDragging = false; // Сбрасываем флаг
        return;
    }

    const $newCard = $(this); // Карточка, на которую кликнули

    // Проверяем, есть ли скрытые карточки
    const $hiddenCards = $('.element-item.hide');
    if ($hiddenCards.length > 0) {
        // Если есть, возвращаем все скрытые карточки в карусель
        $hiddenCards.removeClass('hide hiding').css('display', '');
    setTimeout(() => {
            $hiddenCards.removeClass('showing');
        }, 500); // 500ms - время анимации
    }

    // Добавляем анимацию скрытия новой карточки
    $newCard.addClass('hiding');
    setTimeout(() => {
        $newCard.addClass('hide').removeClass('hiding').css('display', 'none');
    }, 500);

    // Убедимся, что текущая карточка ещё не скрыта
    if (!$newCard.hasClass('hide')) {
        // Добавляем анимацию скрытия новой карточки
        $newCard.addClass('hiding');
        setTimeout(() => {
            $newCard.addClass('hide').css('display', 'none');
        }, 500); // 500ms - время совпадает с анимацией CSS
    }

    // Отображаем данные в блоке активной карточки
    const imageSrc = $newCard.find('img').attr('src');
    const name = $newCard.find('.element-title').text();
    const description = $newCard.find('.full-text').text();
    const action_link = $newCard.find('.action-link').text();

    $('.active-card').show().addClass('showing');
    $('.active-card-image').html(`<img src="${imageSrc}" alt="${name}">`);
    $('.active-card-details').html(`
      <figcaption>${name}</figcaption>
      <p class="active-card-description">${description}</p>
      <figcaption class="action-link">${action_link}</figcaption>
    `);

     // Позиционируем активную карточку поверх карусели только на мобильных устройствах
     if ($(window).width() <= 768) {
      $('.active-card').css({
        position: 'absolute',
        top: $('.element-list').offset().top + 'px',
        left: '50%',  // Центрируем по горизонтали
        transform: 'translateX(-50%)',  // Смещаем назад на 50% от её ширины
        width: '100%',
        zIndex: '999', // Убираем карточку из потока и делаем её поверх карусели
      });
    }

    // Скроллим страницу к активной карточке
    $('html, body').animate({ scrollTop: $('.active-card').offset().top - 50 }, 550);
  });

  // Обработчик клика по ссылке в карточке
  $('.active-card-details').on('click', 'a', function (e) {
    const linkHref = $(this).attr('href');
    
    // Закрытие карточки перед переходом по ссылке
    $('.active-card').removeClass('showing').addClass('hiding');
    setTimeout(() => {
      $('.active-card').hide().removeClass('hiding');
    }, 500);

    // Возвращаем скрытые карточки в карусель
    $('.element-item.hide').each(function () {
      $(this)
          .removeClass('hide hiding showing')
          .addClass('showing')
          .css('display', '');
      setTimeout(() => {
          $(this).removeClass('showing');
      }, 500);
    });
    
    // Переход по ссылке
    setTimeout(() => {
      window.location.href = linkHref;  // Переходим по ссылке после закрытия карточки
    }, 500); // Ожидание завершения анимации скрытия карточки
  });

  // Закрытие активной карточки по клику
  $('.active-card').on('click', function (e) {
    // Останавливаем клик на ссылке, чтобы не срабатывала прокрутка
    if ($(e.target).closest('a').length > 0) {
      return; // Если клик был на ссылке, просто выходим из функции
    }
    
    const $activeCard = $(this); // Селектор активной карточки

    // Скрываем активную карточку с анимацией
    $activeCard.removeClass('showing').addClass('hiding');
    setTimeout(() => {
      $activeCard.hide();
      $activeCard.removeClass('hiding'); // Убираем класс анимации
    }, 500);

    // Возвращаем скрытые карточки в карусель
    $('.element-item.hide').each(function () {
        $(this)
            .removeClass('hide hiding showing')
            .addClass('showing')
            .css('display', '');
        setTimeout(() => {
            $(this).removeClass('showing');
        }, 500);
    });

    // Прокручиваем обратно к карусели
    $('html, body').animate({ scrollTop: $('.element-list').offset().top }, 550);
  });

  // Выравнивание высоты карточек
  function unifyCardHeights() {
    let maxHeight = 0;
    const cards = document.querySelectorAll('.element-item');
    cards.forEach((card) => {
      card.style.height = '';
      maxHeight = Math.max(maxHeight, card.offsetHeight);
    });
    cards.forEach((card) => {
      card.style.height = `${maxHeight}px`;
    });
  }

  // Обновление высот карточек
  $('.element-list').on('setPosition', unifyCardHeights);
  window.addEventListener('load', unifyCardHeights);
  window.addEventListener('resize', unifyCardHeights);
});




