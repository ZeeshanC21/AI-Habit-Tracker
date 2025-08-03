# AI Habit Assistant 🚀

A modern, full-stack web application that uses OpenAI's GPT models to generate personalized 7-day habit-building plans. Built with Flask, featuring a sleek UI and intelligent habit coaching.

![AI Habit Assistant](https://img.shields.io/badge/Flask-3.0.0-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%2F4-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **AI-Powered Plans**: Generate personalized 7-day habit-building plans using OpenAI's GPT models
- **Interactive UI**: Modern, responsive design with smooth animations and micro-interactions
- **Progress Tracking**: Track your daily progress with visual indicators and completion stats
- **Session Management**: In-memory storage for plan persistence during your session
- **Mobile-Responsive**: Optimized for all device sizes
- **Print-Friendly**: Clean printing layout for offline reference
- **Error Handling**: Graceful fallback plans when API is unavailable

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Jinja2
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5.3, Custom CSS with CSS Grid/Flexbox
- **AI Integration**: OpenAI GPT-3.5/GPT-4 API
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Inter)

## 📁 Project Structure

```
ai-habit-assistant/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env.example          # Environment variables template
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page with habit form
│   ├── results.html      # Results page displaying the plan
│   ├── 404.html          # Custom 404 error page
│   └── 500.html          # Custom 500 error page
└── static/
    └── style.css         # Custom CSS styles
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Git (for cloning)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-habit-assistant.git
   cd ai-habit-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
FLASK_SECRET_KEY=your_secret_key_for_sessions
FLASK_DEBUG=True  # Set to False in production
```

### OpenAI API Setup

1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Navigate to API Keys section
3. Create a new API key
4. Add the key to your `.env` file
5. Ensure you have sufficient credits/quota

## 💡 Usage

1. **Enter Your Habits**: Fill in 2-3 habits you want to build (e.g., "Drink 8 glasses of water daily")
2. **Generate Plan**: Click "Generate My Plan" to create your personalized 7-day plan
3. **Follow Daily Tasks**: Each day contains specific tasks and motivational messages
4. **Track Progress**: Mark tasks as complete and watch your progress grow
5. **Print or Save**: Use the print button to save your plan for offline reference

### Example Habits

- **Health**: "Drink 8 glasses of water daily", "Walk 30 minutes every morning"
- **Productivity**: "Read for 20 minutes before bed", "Write in journal for 10 minutes"
- **Wellness**: "Meditate for 5 minutes daily", "Sleep by 10 PM every night"

## 🎨 UI Features

- **Modern Design**: Clean, professional interface with gradients and smooth animations
- **Interactive Elements**: Hover effects, loading states, and micro-interactions
- **Progress Visualization**: Dynamic progress bars and completion statistics
- **Responsive Layout**: Optimized for desktop, tablet, and mobile devices
- **Accessibility**: Proper focus states, semantic HTML, and keyboard navigation

## 🧪 Development

### Running in Development Mode

```bash
export FLASK_DEBUG=True  # On Windows: set FLASK_DEBUG=True
python app.py
```

### Code Structure

- **`app.py`**: Main Flask application with routes and OpenAI integration
- **Templates**: Jinja2 templates with inheritance and modern HTML5
- **Static Files**: Custom CSS with CSS Grid, Flexbox, and animations
- **Error Handling**: Custom 404/500 pages and graceful API fallbacks

### Key Functions

- `generate_habit_plan()`: Integrates with OpenAI API to create personalized plans
- `generate_fallback_plan()`: Provides backup plans when API is unavailable
- Session management for storing plans and user progress

## 🚀 Deployment

### Production Setup

1. **Set production environment variables**
   ```bash
   export FLASK_DEBUG=False
   export FLASK_SECRET_KEY=your_production_secret_key
   ```

2. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

### Platform Deployment

- **Heroku**: Add `Procfile` with `web: gunicorn app:app`
- **Railway**: Direct deployment from GitHub
- **DigitalOcean**: Deploy using App Platform
- **AWS**: Use Elastic Beanstalk or EC2

## 📊 Features Deep Dive

### AI Integration
- Uses OpenAI's chat completion API with structured prompts
- JSON response parsing for consistent plan formatting
- Fallback system ensures app works even without API access
- Customizable AI prompts for different habit types

### Session Management
- In-memory storage for development simplicity
- Session-based plan persistence
- Progress tracking across page refreshes
- Easy to extend to database storage

### UI/UX Excellence
- Mobile-first responsive design
- Smooth CSS animations and transitions
- Interactive progress tracking
- Print-optimized layouts
- Accessibility compliance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Bootstrap team for the excellent CSS framework
- Flask community for the amazing web framework
- Google Fonts for the beautiful Inter typeface

## 📧 Contact

- **GitHub**: [ZeeshanC21](https://github.com/ZeeshanC21)
- **Email**: charoliazeeshan@gmail.com
- **Portfolio**: [zeeshancharolia.com](https://zeeshancharolia.com)

---

Built with ❤️ using Flask and OpenAI • Perfect for portfolios and resume projects