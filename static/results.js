let defaultState = false

const button = document.querySelector('#switch-directions-button').addEventListener('click', () => {
    if (defaultState === false) {
    console.log("click in false")
    document.querySelector('#map').innerHTML = "<img src='/static/img/town_b_to_town_a.png'></img>"
    defaultState = !defaultState
    } else {
        console.log("click in else")
        document.querySelector('#map').innerHTML = "<img src='/static/img/town_a_to_town_b.png'></img>"
        defaultState = !defaultState
  }});
  