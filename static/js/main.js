// Main JavaScript file for Stakeholder Outreach application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Search functionality for stakeholder list
    const searchInput = document.getElementById('stakeholder-search');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const searchTerm = this.value.toLowerCase();
            const stakeholderCards = document.querySelectorAll('.stakeholder-card');
            
            stakeholderCards.forEach(function(card) {
                const name = card.querySelector('.card-title').textContent.toLowerCase();
                const organization = card.querySelector('.organization-text') ? 
                    card.querySelector('.organization-text').textContent.toLowerCase() : '';
                const role = card.querySelector('.role-text') ? 
                    card.querySelector('.role-text').textContent.toLowerCase() : '';
                
                if (name.includes(searchTerm) || organization.includes(searchTerm) || role.includes(searchTerm)) {
                    card.closest('.stakeholder-column').style.display = '';
                } else {
                    card.closest('.stakeholder-column').style.display = 'none';
                }
            });
        });
    }

    // Filter buttons for stakeholder list
    const filterButtons = document.querySelectorAll('.filter-btn');
    if (filterButtons.length > 0) {
        filterButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Add active class to clicked button
                this.classList.add('active');
                
                const filter = this.getAttribute('data-filter');
                const stakeholderCards = document.querySelectorAll('.stakeholder-column');
                
                if (filter === 'all') {
                    stakeholderCards.forEach(card => card.style.display = '');
                } else if (filter === 'recent') {
                    // This is a placeholder - in a real app, you would filter by creation date
                    // For now, just show the first 3 cards as an example
                    stakeholderCards.forEach((card, index) => {
                        card.style.display = index < 3 ? '' : 'none';
                    });
                } else if (filter === 'organization') {
                    // This is a placeholder - in a real app, you would group by organization
                    // For now, just toggle visibility of cards with even/odd indices
                    stakeholderCards.forEach((card, index) => {
                        card.style.display = index % 2 === 0 ? '' : 'none';
                    });
                }
            });
        });
    }

    // Form validation for stakeholder edit form
    const stakeholderForm = document.getElementById('stakeholder-form');
    if (stakeholderForm) {
        stakeholderForm.addEventListener('submit', function(event) {
            if (!this.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            this.classList.add('was-validated');
        });
    }

    // Confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.delete-btn');
    if (deleteButtons.length > 0) {
        deleteButtons.forEach(function(button) {
            button.addEventListener('click', function(event) {
                if (!confirm('Are you sure you want to delete this stakeholder? This action cannot be undone.')) {
                    event.preventDefault();
                }
            });
        });
    }

    // CSV Import validation
    const csvFileInput = document.getElementById('csv_file');
    if (csvFileInput) {
        csvFileInput.addEventListener('change', function() {
            const fileName = this.files[0]?.name;
            if (fileName) {
                // Validate file extension
                if (!fileName.endsWith('.csv')) {
                    alert('Please select a CSV file');
                    this.value = ''; // Clear the file input
                }
            }
        });
        
        const importForm = document.querySelector('form[enctype="multipart/form-data"]');
        if (importForm) {
            importForm.addEventListener('submit', function(event) {
                if (!csvFileInput.files[0]) {
                    event.preventDefault();
                    alert('Please select a CSV file to import');
                }
            });
        }
    }

    // Template download functionality
    window.downloadTemplate = function() {
        const csvContent = "Name,Email,Phone,Organization,Role,Notes\nJohn Doe,john@example.com,555-123-4567,Acme Inc,CEO,Important contact\nJane Smith,jane@example.com,555-987-6543,XYZ Corp,Marketing Director,Met at conference";
        const blob = new Blob([csvContent], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.setAttribute('hidden', '');
        a.setAttribute('href', url);
        a.setAttribute('download', 'stakeholders_template.csv');
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    };

    // Add animation class to cards
    const cards = document.querySelectorAll('.card');
    if (cards.length > 0) {
        cards.forEach(function(card, index) {
            setTimeout(function() {
                card.classList.add('fade-in');
            }, index * 100);
        });
    }
});