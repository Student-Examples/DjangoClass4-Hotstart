$(document).ready(function(){
    Categories.loadAllCats()
})

let Categories = {

    deleteCat: function(id){

        $.ajax({
            url: "http://127.0.0.1:8000/api/categories/"+id+"/",
            type: 'DELETE',
            success: function(result) {
                document.location.reload()
            }
        });
    },

    deleteProduct: function(id){
        $.ajax({
            url: "http://127.0.0.1:8000/api/products/"+id+"/",
            type: 'DELETE',
            success: function(result) {
                document.location.reload()
            }
        });
    },

    loadAllCats: function(){
        $.get("http://127.0.0.1:8000/api/categories/", function(data){
            for(let cat of data){
                $("#categories").append("<div class=\"card\">" +
                    "<header class=\"card-header\">" +
                        "<p data-id='" + cat.id + "' class=\"category card-header-title\">" +
                            cat.id +". "+ cat.name +
                        "</p>" +
                    "</header>" +
                    "<div class=\"card-content\">" +
                        "<div class=\"content\">" +
                            cat.description +
                        "</div>" +
                    "</div>" +
                    "<footer class=\"card-footer\">" +
                        "<a href=\"#\" data-id=\""+cat.id+ "\" class=\"delete-category card-footer-item\">Delete</a>" +
                    "</footer>" +
                "</div>")
            }

            $(".delete-category").on("click", function(){
                let id = $(this).data("id")
                if(confirm("Хотите удалить категорию?")){
                    Categories.deleteCat(id)
                }
            })

            $(".category").on("click", function(){
                let id = $(this).data("id")
                Categories.loadProducts(id)
            })
        })
	},

    loadProducts: function(id){
        $.get("http://127.0.0.1:8000/api/categories/"+id+"/products/", function(data){
            $("#categories").html("")
            $("#products").html("")
            for(let product of data){
                $("#products").append("<div class=\"card\">" +
                    "<header class=\"card-header\">" +
                        "<p data-id='" + product.id + "' class=\"product card-header-title\">" +
                            product.name +
                        "</p>" +
                    "</header>" +
                    "<div class=\"card-content\">" +
                        "<div class=\"content\">" +
                            product.price +" c." +
                        "</div>" +
                    "</div>" +
                    "<footer class=\"card-footer\">" +
                        "<a href=\"#\" data-id=\""+product.id+ "\" class=\"delete-product card-footer-item\">Delete</a>" +
                    "</footer>" +
                "</div>")
            }

            $(".delete-product").on("click", function(){
                let id = $(this).data("id")
                if(confirm("Хотите удалить категорию?")){
                    Categories.deleteProduct(id)
                }
            })
        })
	}
}