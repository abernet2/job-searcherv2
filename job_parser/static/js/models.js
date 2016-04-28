function import_models(model_names) {
    obj = {}
    obj.JobPost = {
        server: '/job_post',

        delete: function(data) {
            var id = data.id;
            var request = $.ajax({
                // this route is for a post, we want to delete
                // a content
                url: [this.server, id].join('/'),
                method: 'DELETE', 
            });

            return request;
        },

        deleteContent: function(data) {
            var temp = this.server;

            return this.delete.call(Content, data);
        },

        edit: function(id, content) {
            return id;
        }
    };

    obj.Content = {
        server: '/job_post/content',

        getEditable: function(id) {
            return $.get([this.server, id, 'edit'].join('/'));
        },

        update: function(id, data) {
            return $.ajax({
                url: [this.server, id].join('/'),
            })
        }
    };

    return obj;
}

