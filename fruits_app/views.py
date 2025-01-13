from django.shortcuts import render, get_object_or_404,redirect
from .models import Product,Category,Blog,Contact,Cart,Comment
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CommentForm




from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.

# def index1(request):
#     return render(request, 'index.html')
def index(request):
    featured_products = Product.objects.all()[:3]
    blog = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'blogs' : blog,
        'featured_products' : featured_products
    }
    return render(request, 'index_2.html', context)
def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            messages.error(request, 'Fields cannot be empty')
        else:
           data = Contact(name=name, email=email, subject=subject, message=message)
           email_subject = f'{subject}: FROM TASTE_QUEST WEBSITE'
           email_data = {
            'name': name,
            'email': email,
            'message': message
           }
           html_message = render_to_string('contact-mail.html', email_data)
           plain_message = strip_tags(html_message)
           from_email = 'TASTE QUEST<abdulkareemtemilayo@gmail.com>'
           recepient_list = [settings.EMAIL_HOST_USER, ]
        try:
            email_message = EmailMessage(email_subject, plain_message, to=recepient_list, from_email=from_email)
            email_message.send()
            data.save
            messages.success(request, 'Message sent successfully')
        except:
            messages.error(request, 'Failed to send message')
            
    return render(request, 'contact.html')

def shop(request):
    product = Product.objects.all()
    page_number = request.GET.get('page') 
    num_per_page = 2  
    paginator = Paginator(product, 5)  # Show 10 products per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.get_page(1)  # Default to the first page

    product = Product.objects.prefetch_related('category').all()
    category = Category.objects.all()
    context = {
        'products': product,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'shop.html',context)

def single_product(request, id):
    product = get_object_or_404(Product, id=id)
    context= {
        'details':product
        }
    return render(request, 'single-product.html',context)
    
def checkout(request):
    return render(request, 'checkout.html')

def blog(request):
    all_blog = Blog.objects.all()
    context = {
        'all_blog': all_blog
    }
    return render(request, 'blog.html', context)

from django.shortcuts import get_object_or_404

def single_blog(request, id):
    # Fetch the blog details
    blog_details = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=blog_details)  # Fetch comments related to the blog

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog_details  # Link the comment to the blog
            comment.save()
            messages.success(request, "Your review has been submitted.")
        else:
            messages.error(request, "There was an error with your review. Please try again.")
    else:
        comment_form = CommentForm()

    # Prepare the context for rendering
    context = {
        "blog_details": blog_details,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, "single-blog.html", context)


    # context = {
    #         "blog_details": blog_details,
    #         "comments": comments,
    #         "comment_form": comment_form,
    #     }
    #     return render(request, 'single_blog.html', context)

    # blog_details = get_object_or_404(Blog, id=id)
    # reviews = Review.objects.filter(blog=blog_details).order_by('-created_at')  # Get reviews related to the blog

    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)  # Create an instance but don't save it yet
    #         review.blog = blog_details  # Associate the review with the blog
    #         review.save()  # Now save the review
    #         return redirect('single_blog', id=id)  # Redirect to the same page to show the new comment
    # else:
    #     form = ReviewForm()  # Initialize an empty form

    # context = {
    #     'blog_details': blog_details,
    #     'reviews': reviews,  # Fix the spelling error from 'reiews' to 'reviews'
    #     'form': form
    # }
    # return render(request, 'single-blog.html', context)


