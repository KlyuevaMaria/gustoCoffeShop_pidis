// Боковая навигация

// Получение всех элементов навигации
var navItems = document.querySelectorAll('.changeCol');

// Итерация по всем элементам навигации
navItems.forEach(function (navItem) {
    // Добавление обработчика события наведения
    navItem.addEventListener('mouseenter', function () {
        this.style.backgroundColor = "#ECA852";
        // Увеличение области выделения
        this.style.padding = '5px 10px';
        // Закругление краев
        this.style.borderRadius = '4px';
        this.style.transition = '0.35s';
    });

    // Добавление обработчика события ухода курсора
    navItem.addEventListener('mouseleave', function () {
        // Возвращение исходных значений
        this.style.backgroundColor = "";
        this.style.padding = '';
        this.style.borderRadius = '';
    });
});



// Получаем все элементы с классом 'card'
var cards = document.getElementsByClassName('card');

// Для каждого элемента
for (var i = 0; i < cards.length; i++) {
  // Добавляем обработчик события наведения курсора мыши
  cards[i].addEventListener('mouseover', showText);
  // Добавляем обработчик события ухода курсора мыши
  cards[i].addEventListener('mouseout', hideText);
}

// Функция для показа текста
function showText() {
  var cardBody = this.querySelector('.cardDesc');
  cardBody.style.display = 'block';
}

// Функция для скрытия текста
function hideText() {
  var cardBody = this.querySelector('.cardDesc');
  cardBody.style.display = 'none';
}
