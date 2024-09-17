from django.shortcuts import render

def resume_view(request):
    return render(request, 'resume.html')  # Render the template for your resume

