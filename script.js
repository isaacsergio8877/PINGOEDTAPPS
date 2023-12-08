let menu = document.querySelector('#menu-icon');
let navlinks = document.querySelector('.nav-links');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlinks.classList.toggle('open')
}

function performSearch() {
    // Obter o valor digitado na barra de pesquisa
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();

    // Obter todas as divs com a classe "searchable"
    var searchables = document.querySelectorAll('.searchable');

    // Iterar sobre as divs e ocultar aquelas que não correspondem ao termo de pesquisa
    searchables.forEach(function (div) {
        var textContent = div.textContent.toLowerCase();
        if (textContent.includes(searchTerm)) {
            // Exibir div se contiver o termo de pesquisa
            div.classList.remove('hidden');
        } else {
            // Ocultar div se não contiver o termo de pesquisa
            div.classList.add('hidden');
        }
    });
}
