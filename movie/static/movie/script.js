$(document).ready(function)(){
	$('.show-form').click(function(){
		$.ajax({
			url: 'create/',
			type: 'get',
			dataType: 'json',
			beforeSend: function(){
				$('#modal-movie').modal('show')
			},
			success: function(data){
				$('#modal-movie .modal-content').html(data.html_form);
			}
		})
	})
}