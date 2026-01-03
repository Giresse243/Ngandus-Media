/**
 * Ngandus Media - API Integration
 * Connects frontend to Django backend for dynamic content loading
 */

const API_BASE_URL = 'http://localhost:8000/api';

// Load all content on page load
document.addEventListener('DOMContentLoaded', function () {
    loadAllContent();
    setupNewsletterForm();
    setupContactForm();
    setupBookingForm();
});

/**
 * Load all site content from API
 */
async function loadAllContent() {
    try {
        const response = await fetch(`${API_BASE_URL}/content/all/`);
        if (!response.ok) {
            console.log('API not available, using static content');
            return;
        }
        const data = await response.json();

        // Update Hero Section
        if (data.hero && Object.keys(data.hero).length > 0) {
            updateHeroSection(data.hero);
        }

        // Update About Section
        if (data.about && Object.keys(data.about).length > 0) {
            updateAboutSection(data.about);
        }

        // Update Site Settings (footer, social links)
        if (data.settings && Object.keys(data.settings).length > 0) {
            updateSiteSettings(data.settings);
        }

        // Update Countdown
        if (data.countdown && Object.keys(data.countdown).length > 0) {
            updateCountdown(data.countdown);
        }

        // Update Videos
        if (data.videos && data.videos.length > 0) {
            updateVideos(data.videos);
        }

        // Update Events
        if (data.events && data.events.length > 0) {
            updateEvents(data.events);
        }

        // Update Services (dynamic from admin)
        if (data.services && data.services.length > 0) {
            updateServices(data.services);
        }

    } catch (error) {
        console.log('Using static content - API not available:', error.message);
    }
}

/**
 * Update Services Section with API data
 */
function updateServices(services) {
    const servicesContainer = document.getElementById('services-container');
    if (!servicesContainer) return;

    // Clear existing static content
    servicesContainer.innerHTML = '';

    services.forEach(service => {
        const priceDisplay = service.price
            ? `<span style="color: #ffc107; font-size: 18px; font-weight: bold;">${service.price_description || 'From'} R${Number(service.price).toLocaleString()}</span>`
            : '';

        const imageUrl = service.icon || 'img/services/service-1.png';

        const serviceCard = `
            <div class="col-lg-4 col-md-6 col-sm-6">
                <div class="discography__item">
                    <div class="discography__item__pic">
                        <img src="${imageUrl}" alt="${service.title}">
                    </div>
                    <div class="discography__item__text">
                        ${priceDisplay}
                        <h4>${service.title}</h4>
                        <p>${service.description}</p>
                        <a href="./booking.html" class="primary-btn">Book Now</a>
                    </div>
                </div>
            </div>
        `;
        servicesContainer.innerHTML += serviceCard;
    });
}

/**
 * Update Hero Section with API data
 */
function updateHeroSection(hero) {
    const heroSection = document.getElementById('hero-section');
    if (heroSection && hero.background_image) {
        heroSection.setAttribute('data-setbg', hero.background_image);
    }

    const heroTitle = document.getElementById('hero-title');
    if (heroTitle && hero.title) heroTitle.textContent = hero.title;

    const heroSubtitle = document.getElementById('hero-subtitle');
    if (heroSubtitle && hero.subtitle) heroSubtitle.textContent = hero.subtitle;

    const heroDesc = document.getElementById('hero-description');
    if (heroDesc && hero.description) heroDesc.innerHTML = hero.description;

    const heroVideo = document.getElementById('hero-video');
    if (heroVideo && hero.video_url) heroVideo.href = hero.video_url;
}

/**
 * Update About Section with API data
 */
function updateAboutSection(about) {
    const aboutTitle = document.getElementById('about-title');
    if (aboutTitle && about.title) aboutTitle.textContent = about.title;

    const aboutSubtitle = document.getElementById('about-subtitle');
    if (aboutSubtitle && about.subtitle) aboutSubtitle.textContent = about.subtitle;

    const aboutDesc = document.getElementById('about-description');
    if (aboutDesc && about.description) aboutDesc.textContent = about.description;

    const aboutImage = document.getElementById('about-image');
    if (aboutImage && about.image) aboutImage.src = about.image;

    const aboutButton = document.getElementById('about-button');
    if (aboutButton) {
        if (about.button_text) aboutButton.textContent = about.button_text;
        if (about.button_url) aboutButton.href = about.button_url;
    }
}

/**
 * Update Site Settings (footer)
 */
function updateSiteSettings(settings) {
    const footerPhone = document.getElementById('footer-phone');
    if (footerPhone && settings.phone) footerPhone.textContent = settings.phone;

    const footerEmail = document.getElementById('footer-email');
    if (footerEmail && settings.email) footerEmail.textContent = settings.email;

    // Social links
    if (settings.facebook_url) {
        const fb = document.getElementById('footer-facebook');
        if (fb) fb.href = settings.facebook_url;
    }
    if (settings.twitter_url) {
        const tw = document.getElementById('footer-twitter');
        if (tw) tw.href = settings.twitter_url;
    }
    if (settings.instagram_url) {
        const ig = document.getElementById('footer-instagram');
        if (ig) ig.href = settings.instagram_url;
    }
    if (settings.youtube_url) {
        const yt = document.getElementById('footer-youtube');
        if (yt) yt.href = settings.youtube_url;
    }
}

/**
 * Update Countdown Section
 */
function updateCountdown(countdown) {
    const countdownTitle = document.getElementById('countdown-title');
    if (countdownTitle && countdown.title) countdownTitle.textContent = countdown.title;

    const countdownSubtitle = document.getElementById('countdown-subtitle');
    if (countdownSubtitle && countdown.subtitle) countdownSubtitle.textContent = countdown.subtitle;

    const countdownButton = document.getElementById('countdown-button');
    if (countdownButton) {
        if (countdown.button_text) countdownButton.textContent = countdown.button_text;
        if (countdown.button_url) countdownButton.href = countdown.button_url;
    }

    // Update countdown timer if event_date is provided
    if (countdown.event_date) {
        // This would integrate with the existing countdown plugin
        console.log('Countdown date:', countdown.event_date);
    }
}

/**
 * Update Video Gallery
 */
function updateVideos(videos) {
    const videoContainer = document.querySelector('.youtube .row:last-child');
    if (!videoContainer || videos.length === 0) return;

    // Clear existing videos except structure
    const existingVideos = videoContainer.querySelectorAll('.col-lg-4');

    videos.slice(0, 3).forEach((video, index) => {
        if (existingVideos[index]) {
            const item = existingVideos[index].querySelector('.youtube__item');
            if (item) {
                const pic = item.querySelector('.youtube__item__pic');
                if (pic && video.thumbnail) {
                    pic.setAttribute('data-setbg', video.thumbnail);
                }
                const link = pic.querySelector('a');
                if (link && video.video_url) {
                    link.href = video.video_url;
                }
                const title = item.querySelector('.youtube__item__text h4');
                if (title && video.title) {
                    title.textContent = video.title;
                }
            }
        }
    });
}

/**
 * Update Events Section
 */
function updateEvents(events) {
    // Events would be updated in the event slider
    console.log('Events loaded:', events.length);
}

/**
 * Setup Newsletter Form
 */
function setupNewsletterForm() {
    const form = document.getElementById('newsletter-form');
    if (!form) return;

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const emailInput = document.getElementById('newsletter-email');
        const email = emailInput.value;

        try {
            const response = await fetch(`${API_BASE_URL}/contact/newsletter/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email }),
            });

            const data = await response.json();
            alert(data.message || 'Thank you for subscribing!');
            emailInput.value = '';
        } catch (error) {
            alert('Thank you for subscribing!');
            emailInput.value = '';
        }
    });
}

/**
 * Setup Contact Form (if on contact page)
 */
function setupContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = {
            name: document.getElementById('contact-name')?.value,
            email: document.getElementById('contact-email')?.value,
            subject: document.getElementById('contact-subject')?.value,
            message: document.getElementById('contact-message')?.value,
        };

        try {
            const response = await fetch(`${API_BASE_URL}/contact/send/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const data = await response.json();
            alert(data.message || 'Message sent successfully!');
            form.reset();
        } catch (error) {
            alert('Thank you for your message!');
            form.reset();
        }
    });
}

/**
 * Setup Booking Form (if on booking page)
 */
function setupBookingForm() {
    const form = document.getElementById('booking-form');
    if (!form) return;

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = {
            name: document.getElementById('booking-name')?.value,
            email: document.getElementById('booking-email')?.value,
            phone: document.getElementById('booking-phone')?.value,
            service: document.getElementById('booking-service')?.value,
            preferred_date: document.getElementById('booking-date')?.value,
            preferred_time: document.getElementById('booking-time')?.value,
            message: document.getElementById('booking-message')?.value,
        };

        try {
            const response = await fetch(`${API_BASE_URL}/bookings/create/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const data = await response.json();
            alert(data.message || 'Booking request submitted successfully!');
            form.reset();
        } catch (error) {
            alert('Booking request submitted!');
            form.reset();
        }
    });
}
