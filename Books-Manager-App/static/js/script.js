// Main JavaScript file for book management website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize any tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Quick price update functionality
    const priceUpdateForms = document.querySelectorAll('.price-update-form');
    priceUpdateForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const isbn = this.dataset.isbn;
            const priceInput = document.getElementById(`price-${isbn}`);
            const newPrice = parseFloat(priceInput.value);
            
            // Validate price is a positive number
            if (isNaN(newPrice) || newPrice <= 0) {
                showAlert('Price must be a positive number', 'danger');
                return;
            }
            
            // Send AJAX request to update price
            fetch('/api/update_price', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    isbn: isbn,
                    price: newPrice
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('Price updated successfully', 'success');
                    // Update the displayed price in the table
                    const priceCell = document.querySelector(`#book-${isbn} .book-price`);
                    if (priceCell) {
                        priceCell.textContent = `$${newPrice.toFixed(2)}`;
                    }
                } else {
                    showAlert('Failed to update price: ' + data.message, 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('An error occurred while updating the price', 'danger');
            });
        });
    });

    // Standardize genres button functionality
    const standardizeButton = document.getElementById('standardize-genres');
    if (standardizeButton) {
        standardizeButton.addEventListener('click', function() {
            fetch('/api/standardize_genres', {
                method: 'POST',
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('Genres standardized successfully', 'success');
                    // Reload the page to see updates
                    setTimeout(() => {
                        window.location.reload();
                    }, 1000);
                } else {
                    showAlert('Failed to standardize genres', 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('An error occurred while standardizing genres', 'danger');
            });
        });
    }

    // Delete book confirmation
    const deleteButtons = document.querySelectorAll('.delete-book');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this book?')) {
                e.preventDefault();
            }
        });
    });

    // Function to show alerts
    function showAlert(message, type) {
        const alertsContainer = document.getElementById('alerts-container');
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.role = 'alert';
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        alertsContainer.appendChild(alert);
        
        // Auto dismiss after 3 seconds
        setTimeout(() => {
            alert.classList.remove('show');
            setTimeout(() => {
                alertsContainer.removeChild(alert);
            }, 150);
        }, 3000);
    }

    // Genre input enhancement
    const genreInput = document.getElementById('genres');
    if (genreInput) {
        genreInput.addEventListener('blur', function() {
            // Clean up genres input - lowercase and trim spaces
            const genres = this.value.split(',')
                .map(genre => genre.trim().toLowerCase())
                .filter(genre => genre)
                .join(', ');
            this.value = genres;
        });
    }

    // Search form placeholder animation
    const searchInput = document.getElementById('author-search');
    if (searchInput) {
        const placeholders = [
            'Search by author...',
            'Try "Jane Austen"...',
            'Search for "Orwell"...',
            'Find books by author...'
        ];
        let currentPlaceholder = 0;
        
        // Change placeholder every 3 seconds
        setInterval(() => {
            currentPlaceholder = (currentPlaceholder + 1) % placeholders.length;
            searchInput.setAttribute('placeholder', placeholders[currentPlaceholder]);
        }, 3000);
    }
});
