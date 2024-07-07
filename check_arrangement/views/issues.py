from django.shortcuts import get_object_or_404, redirect, render, reverse
from django_ratelimit.decorators import ratelimit

from check_arrangement.models import Apartment, ApartmentIssue
from check_arrangement.forms import IssueForm


@ratelimit(key='ip')
def add_issue(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        form = IssueForm(request.POST, apartment=apartment,)
        rendered_form = form.render("check_arrangement/snippets/form_add_issue_snippet.html")
        if form.is_valid():
            form.instance.apartment = apartment
            form.save()
            return redirect(f"{reverse('check_arrangement:add_issue', kwargs={'apartment_id': apartment.id})}?success=1")
    else:
        form = IssueForm(apartment=apartment, label_suffix='')
        rendered_form = form.render("check_arrangement/snippets/form_add_issue_snippet.html")
    context = {
        'apartment': apartment,
        'form': rendered_form
    }

    return render(request, 'check_arrangement/add_issue.html', context)


def delete_issue(request, apartmentissue_id):
    issue = get_object_or_404(ApartmentIssue, id=apartmentissue_id)
    issue.delete()
    return redirect('check_arrangement:results', apartment_id=issue.apartment.id)