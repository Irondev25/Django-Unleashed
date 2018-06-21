from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic import View


class ObjectUpdateMixin(View):
    template_name = ''
    model = None
    form_class = None

    def get(self, request, slug):
        object = get_object_or_404(self.model, slug=slug)
        form = self.form_class(instance=object)
        context = {
            'form': form,
            self.model.__name__.lower(): object
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        object = get_object_or_404(self.model, slug=slug)
        bound_form = self.form_class(request.POST, instance=object)
        context={
            'form':bound_form,
            self.model.__name__.lower():object
        }
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(request, self.template_name, context)


class ObjectDeleteMixin(View):
    template_name = ''
    model = None
    success_url = ''

    def get(self, request, slug):
        object = get_object_or_404(self.model, slug=slug)
        return render(request, self.template_name, {self.model.__name__.lower():object})

    def post(self, request, slug):
        object = get_object_or_404(self.model, slug=slug)
        object.delete()
        return HttpResponseRedirect(self.success_url)



class SlugCleanMixin:
    """Mixin class for slug cleaning method"""

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise forms.ValidationError("Slug can't be 'create'.")
        return new_slug

