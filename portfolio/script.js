document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Scrolled Header State
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // 2. Mobile Menu Toggle
  const menuToggle = document.getElementById('menu-toggle-btn');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  menuToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('open');
    menuToggle.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', isOpen);
  });

  // Close menu when clicking links
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      menuToggle.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });

  // 3. Project Filtering Logic
  const tabButtons = document.querySelectorAll('.tab-btn');
  const projectCards = document.querySelectorAll('.project-card');

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Set active tab button
      tabButtons.forEach(btn => {
        btn.classList.remove('active');
        btn.setAttribute('aria-selected', 'false');
      });
      button.classList.add('active');
      button.setAttribute('aria-selected', 'true');

      const filterValue = button.getAttribute('data-filter');

      // Filter cards
      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        
        if (filterValue === 'all' || category === filterValue) {
          card.style.display = 'block';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 10);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });

  // Add transition styling properties to cards dynamically
  projectCards.forEach(card => {
    card.style.transition = 'opacity 0.25s ease, transform 0.25s ease, border-color 0.3s ease, box-shadow 0.3s ease';
  });

  // 4. Scroll-driven Nav Link Active State (IntersectionObserver)
  const sections = document.querySelectorAll('section');
  const observerOptions = {
    root: null,
    rootMargin: '-30% 0px -60% 0px', // Trigger when section is in the middle of the viewport
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const activeId = entry.target.getAttribute('id');
        
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${activeId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => {
    sectionObserver.observe(section);
  });

  // 5. Mock Contact Form Submission
  const contactForm = document.getElementById('contact-form');
  const formFeedback = document.getElementById('form-feedback');
  const submitButton = document.getElementById('form-submit-btn');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Basic validation
      const name = document.getElementById('form-name').value.trim();
      const email = document.getElementById('form-email').value.trim();
      const message = document.getElementById('form-message').value.trim();

      if (!name || !email || !message) {
        showFeedback('Please fill out all fields.', 'error');
        return;
      }

      // Update button state
      submitButton.disabled = true;
      submitButton.textContent = 'Sending...';
      formFeedback.className = 'form-feedback-message';
      formFeedback.textContent = '';

      // Simulate network request
      setTimeout(() => {
        submitButton.disabled = false;
        submitButton.textContent = 'Send Message';
        showFeedback('Thank you! Your message has been sent successfully.', 'success');
        contactForm.reset();
      }, 1200);
    });
  }

  function showFeedback(text, type) {
    formFeedback.textContent = text;
    formFeedback.className = `form-feedback-message ${type}`;
    
    // Clear message after 5 seconds if success
    if (type === 'success') {
      setTimeout(() => {
        formFeedback.style.opacity = '0';
        setTimeout(() => {
          formFeedback.textContent = '';
          formFeedback.style.opacity = '1';
          formFeedback.className = 'form-feedback-message';
        }, 300);
      }, 5000);
    }
  }

  // 6. Progressive Enhancement: Fallback scroll animations for browsers without native CSS scroll timelines
  if (!CSS.supports('(animation-timeline: view()) and (animation-range: entry)')) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            revealObserver.unobserve(entry.target); // Animate once
          }
        });
      },
      {
        rootMargin: '0px 0px -10% 0px', // Trigger slightly before coming fully into view
        threshold: 0.15
      }
    );

    document.querySelectorAll('.scroll-reveal').forEach((el) => {
      // Set initial styles for fallback browsers
      el.style.opacity = '0';
      el.style.transform = 'translateY(30px)';
      el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      revealObserver.observe(el);
    });
  }
});
