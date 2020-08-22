$(document).ready(function(){
    $('#add-form').submit(function(e){
      e.preventDefault()
      const url = $(this).attr('action')
      const maindiv = $('.main-contents')
      $.ajax({
        type:'POST',
        url:url,
        data:{
          'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
          'contents':$('input[name=contents]').val()
        },
        success:function(response){
          maindiv.append('<div class="mx-auto card border-success mb-3" style="max-width: 18rem;"><div class="text-left text-success"><p class="text-dark ml-3 mt-1 mb-1">'+response.contents +'</p></div></div>')
        },
        error:function(error){
          console.log(error)
        }
      })
      this.reset()
    })
  })