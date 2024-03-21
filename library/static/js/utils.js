
document.addEventListener('DOMContentLoaded', function() {
  onClicked();
})

function onClicked(){
  const click = document.getElementById('click')
  console.log(click)
}

function alertReserve() {
  if (document.body.textContent.includes('Parabéns, você agendou o livo')) {
    Swal.fire({
      title:"Parabéns",
      text: "Livro agendado com Sucesso",
      icon: "success",
    });
  } else if(document.body.textContent.includes('Você já tem um livro agendado'))
    Swal.fire({
      title: "Descuple",
      text: "Você já tem um livro agendado",
      icon: "error"
    });
}

document.addEventListener('DOMContentLoaded', function() {
  alertReserve(); 
});

function alertRenewReserve(){
  if(document.body.textContent.includes('Livro renovado com sucesso')){
    Swal.fire({
      title: "Renovado",
      text: "Livro renovado com sucesso",
      icon: "success",
    })
  }
}

document.addEventListener('DOMContentLoaded', function(){
  alertRenewReserve();
});

function alertReserveBookDevolution() {
  if(document.body.textContent.includes('Livro devolvido com sucesso.')){
    Swal.fire({
      title: "Devolvido",
      text: "Livro devolvido com sucesso",
      icon: "success"
    })
  }else if(document.body.textContent.includes('Você não possui livro reservado')){
    Swal.fire({
      title: "Descuple",
      text: "Você não possui nenhum livro agendado",
      icon: "error",
    })
  } 
}

document.addEventListener('DOMContentLoaded', function(){
  alertReserveBookDevolution();
});

function alertCommentCreate(){
  if(document.body.textContent.includes('Comentário adicionado com sucesso! Obrigado por expor sua opinião')){
    Swal.fire({
      title: "Sucesso",
      text: "Comentário adicionado com sucesso",
      icon: "success",
    })
  }
}

document.addEventListener('DOMContentLoaded', function(){
  alertCommentCreate();
});

