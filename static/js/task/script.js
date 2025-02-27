


// edit task

// edit tasl\k


function editTask(taskId) {
    fetch(`/task/edit/${taskId}/`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('editTaskModalContent').innerHTML = data;
            $('#editTaskModal').modal('show');
        });
}


function deleteTask(taskId) {
  if (confirm("Êtes-vous sûr de vouloir supprimer cette tâche ?")) {
    fetch(`/task/delete/${taskId}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'), // Important pour Django
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        // Supprimer l'élément de la tâche de la page
        const taskElement = document.getElementById(`task-${taskId}`);
        if (taskElement) {
          taskElement.remove();
          alert("Tâche supprimée avec succès.");
        }
      } else {
        alert("Erreur lors de la suppression de la tâche.");
        console.error("Erreur lors de la suppression :", data.message); 
        alert(`Erreur lors de la suppression de la tâche: ${data.message}`); // 
      }
    });
  }
}

  // Fonction pour récupérer le token CSRF (nécessaire pour Django)
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Est-ce que ce cookie correspond au nom que nous recherchons ?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }


  document.getElementById('editTaskModalContent').addEventListener('click', function(event) {
            if (event.target.id === 'saveTaskButton') {
                const form = document.getElementById('editTaskForm');
                const formData = new FormData(form);
                fetch('{% url "task:edit_task" task.id %}', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        document.getElementById(`task-{{ task.id }}`).querySelector('.card-header span:first-child').textContent = data.task.title;
                        document.getElementById(`task-{{ task.id }}`).querySelector('.card-body p').textContent = data.task.content;
                        document.getElementById(`task-{{ task.id }}`).querySelector('.card-header span:last-child').textContent = data.task.status;
                        $('#editTaskModal').modal('hide');
                    } else {
                        alert(data.message || 'Erreur lors de la modification de la tâche.');
                    }
                });
            }
        });

// function editTask(taskId) {
//     console.log("editTask appelé avec taskId :", taskId); // Vérifier que la fonction est appelée
//     fetch(`/task/edit/${taskId}/`)
//         .then(response => {
//             console.log("Réponse reçue :", response); // Vérifier la réponse
//             return response.text();
//         })
//         .then(data => {
//             console.log("Données reçues :", data); // Vérifier les données
//             document.getElementById('editTaskModalContent').innerHTML = data;
//             $('#editTaskModal').modal('show');
//         })
//         .catch(error => {
//             console.error("Erreur lors de la requête :", error); // Vérifier les erreurs
//         });
// }

// Template model
    // document.getElementById('saveTaskButton').addEventListener('click', function() {
    //     const form = document.getElementById('editTaskForm');
    //     const formData = new FormData(form);
    //     fetch('{% url "task:edit_task" task.id %}', {
    //         method: 'POST',
    //         body: formData,
    //         headers: {
    //             'X-CSRFToken': formData.get('csrfmiddlewaretoken')
    //         }
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         if (data.status === 'success') {
    //             document.getElementById(`task-{{ task.id }}`).querySelector('.card-header span:first-child').textContent = data.task.title;
    //             document.getElementById(`task-{{ task.id }}`).querySelector('.card-body p').textContent = data.task.content;
    //             document.getElementById(`task-{{ task.id }}`).querySelector('.card-header span:last-child').textContent = data.task.status;
    //             $('#editTaskModal').modal('hide'); // Fermer le modal
    //         } else {
    //             alert('Erreur lors de la modification de la tâche.');
    //         }
    //     });
    // });
// End template modal

