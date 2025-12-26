// CEREMAC - JavaScript Professionnel avec Animations

document.addEventListener('DOMContentLoaded', function() {
    // Animation au scroll avec Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }, index * 100);
            }
        });
    }, observerOptions);

    // Observer tous les éléments avec la classe 'observe' ou les cards
    document.querySelectorAll('.card, .hero-card, .stat-item, .publication-item, .news-card').forEach(el => {
        observer.observe(el);
    });

    // Navbar scroll effect
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });

    // Smooth scroll pour les ancres
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Gestion du formulaire de contact avec validation
    const contactForm = document.querySelector('#contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validation côté client
            const name = this.querySelector('[name="name"]').value.trim();
            const email = this.querySelector('[name="email"]').value.trim();
            const subject = this.querySelector('[name="subject"]').value.trim();
            const message = this.querySelector('[name="message"]').value.trim();
            
            if (!name || !email || !subject || !message) {
                showAlert('danger', 'Veuillez remplir tous les champs.');
                return;
            }
            
            if (!validateEmail(email)) {
                showAlert('danger', 'Veuillez entrer une adresse email valide.');
                return;
            }
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading"></span> Envoi en cours...';
            
            const formData = new FormData(this);
            const actionUrl = this.getAttribute('data-ajax-url') || 'contact-handler.php';
            
            fetch(actionUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('success', data.message);
                    this.reset();
                } else {
                    showAlert('danger', data.message);
                }
            })
            .catch(error => {
                showAlert('danger', 'Erreur lors de l\'envoi du message. Veuillez réessayer.');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            });
        });
    }

    // Gestion de la newsletter
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = this.querySelector('[name="email"]').value.trim();
            
            if (!email) {
                showAlert('danger', 'Veuillez entrer votre adresse email.');
                return;
            }
            
            if (!validateEmail(email)) {
                showAlert('danger', 'Veuillez entrer une adresse email valide.');
                return;
            }
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading"></span>';
            
            const formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('success', data.message);
                    this.reset();
                } else {
                    showAlert('danger', data.message);
                }
            })
            .catch(error => {
                showAlert('danger', 'Erreur lors de l\'inscription. Veuillez réessayer.');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            });
        });
    }

    // Fonction pour afficher les alertes avec animation
    function showAlert(type, message) {
        // Supprimer les alertes existantes
        const existingAlerts = document.querySelectorAll('.alert-toast');
        existingAlerts.forEach(alert => alert.remove());
        
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-toast alert-dismissible fade show position-fixed`;
        alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px; max-width: 500px; box-shadow: 0 5px 20px rgba(0,0,0,0.2); animation: slideInRight 0.3s ease-out;';
        alertDiv.innerHTML = `
            <strong>${type === 'success' ? '✓' : '✗'}</strong> ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.body.appendChild(alertDiv);
        
        setTimeout(() => {
            alertDiv.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => alertDiv.remove(), 300);
        }, 5000);
    }

    // Validation email
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Animation des statistiques (compteur)
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        const target = parseInt(stat.textContent.replace(/\D/g, ''));
        if (target > 0) {
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    stat.textContent = target + '+';
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(current) + '+';
                }
            }, 30);
        }
    });

    // Parallax effect pour hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            if (scrolled < heroSection.offsetHeight) {
                heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
        });
    }

    // Lazy loading des images avec intersection observer
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.add('fade-in');
                        observer.unobserve(img);
                    }
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Animation des icônes au hover
    document.querySelectorAll('.hero-card i, .card i').forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
        });
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });

    // Ajout d'animations CSS dynamiques
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
        
        .hero-card i, .card i {
            transition: transform 0.3s ease;
        }
    `;
    document.head.appendChild(style);
});
