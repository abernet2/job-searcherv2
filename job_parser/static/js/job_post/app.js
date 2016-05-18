$(document).ready(function(){
    var $button = $('form[action="parse"]'),
        text = 'loading';

    function getMorePosts(evt) {
        evt.preventDefault();

        flipButton();

        $.ajax({
            method: $button.attr('method'),
            url: $button.attr('action')
        })
        .then(formatPosts)
        .done(insertPosts)
    }

    function formatPosts(posts) {
        posts = JSON.parse(posts);
        return posts.map(function(post){
            if(!post) return null;
            var html = ['<li>', '<a ', 'href=', post.id, '>', post.position, '</a></li>'].join('');
            return $(html).addClass('new-post');
        })
    }

    function insertPosts(posts) {
        flipButton();
        posts.forEach(function(post){
            $('ul').prepend(post);
            console.log(post);
        });
    }

    function flipButton() {
        var temp = $button.children('input').attr('value');
        $button.children('input').attr('value', text);
        text = temp;
    }

    $button.on('submit', getMorePosts);

});