const likeButtons = document.querySelectorAll('.js-like-buttons')

likeButtons.forEach(likeButton => {
    likeButton.addEventListener('click', function(event){
        const URL = `${event.target.dataset.id}/like/`;
        axios.get(URL)
            .then((res) => {
                if (res.data.liked) {
                    event.target.classList.remove('far')
                    event.target.classList.add('fas')
                }
                else { // 지금 좋아요 해제 
                    event.target.classList.remove('fas')
                    event.target.classList.add('far')
                }
            }
        )
    })
})

for (likeButton of likeButtons) {
    console.log(likeButton)
}