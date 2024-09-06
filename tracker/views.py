from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, SubCategory, Contribution


def homepage(request):
    return redirect('category_list')  # Redirect to the category list page or whichever page you'd like as the homepage


def contributions_list(request):
    # Retrieve all contributions
    contributions = Contribution.objects.select_related('subcategory').all()

    # Retrieve all subcategories
    all_subcategories = SubCategory.objects.all()

    # Create a list to track subcategories with no or incomplete contributions
    pending_subcategories = []

    for subcategory in all_subcategories:
        current_volunteer_count = subcategory.contributions.count()

        if current_volunteer_count < subcategory.max_volunteers:
            pending_subcategories.append({
                'subcategory': subcategory,
                'status': 'Pending',  # Still needs volunteers
                'current_volunteers': current_volunteer_count
            })
        else:
            pending_subcategories.append({
                'subcategory': subcategory,
                'status': 'quantités déja requises',  # Max volunteers reached
                'current_volunteers': current_volunteer_count
            })

    context = {
        'contributions': contributions,
        'pending_subcategories': pending_subcategories,
    }
    return render(request, 'tracker/contributions_list.html', context)



def category_list(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category', None)

    # Initialize subcategories as an empty list to avoid NoneType errors
    subcategories = []

    if selected_category_id:
        try:
            selected_category = Category.objects.get(id=selected_category_id)
            subcategories = selected_category.subcategories.all()

            # Handle form submission for subcategories
            if request.method == 'POST':
                subcategory_id = request.POST.get('subcategory_id')
                subcategory = SubCategory.objects.get(id=subcategory_id)

                # Check the current number of volunteers for this subcategory
                current_volunteers = subcategory.contributions.count()
                if current_volunteers >= subcategory.max_volunteers:
                    # Show a warning if max volunteers reached
                    messages.warning(request, f"Max number of volunteers reached for {subcategory.name}!")
                else:
                    # Create a new contribution
                    quantity = request.POST.get('quantity')
                    volunteer = request.POST.get('volunteer')
                    comment = request.POST.get('comment')

                    Contribution.objects.create(
                        subcategory=subcategory,
                        quantity=quantity,
                        volunteer=volunteer,
                        comment=comment,
                    )

                    # Success message
                    messages.success(request, f"{volunteer}'s contribution to {subcategory.name} has been added successfully!")

                # Redirect to reset form values after submission
                return redirect(f'/tracker/categories/?category={selected_category_id}')

        except Category.DoesNotExist:
            selected_category = None
            subcategories = []

    else:
        selected_category = None

    # Reset form values if not POST request
    for subcategory in subcategories:
        subcategory.quantity = None
        subcategory.volunteer = ''
        subcategory.comment = ''

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'subcategories': subcategories,
    }
    return render(request, 'tracker/category_list.html', context)
