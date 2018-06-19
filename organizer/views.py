from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Tag, Startup, Newslink
from .forms import TagForm, NewslinkForm, StartupForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin





views relate to Tag.
 def tag_list(request):
     return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})



def tag_detail(request, slug):
    context = {'tag': get_object_or_404(Tag, slug__iexact=slug)}
    return render(request, 'organizer/tag_detail.html', context=context)


# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#         else:
#             return render(request, 'organizer/tag_create.html', context={'form': form})
#     else:
#         form = TagForm()
#         return render(request, 'organizer/tag_create.html', context={'form': form})

class TagCreate(ObjectCreateMixin ,View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    template_name = 'organizer/tag_form_update.html'
    model = Tag
    form_class = TagForm


class TagDelete(ObjectDeleteMixin, View):
    template_name = 'organizer/tag_confirm_delete.html'
    model = Tag
    success_url = reverse_lazy('organizer:tag_list')


#views relate to startup
# def startup_list(request):
#     return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})
class StartupList(View):
    template_name = 'organizer/startup_list.html'
    model = Startup
    paginate_by = 5
    page_kwarg = 'page'

    def get(self, request):
        startups = self.model.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        #if next page is available
        if page.has_next():
            next_url = "?{page}={n}".format(
                page=self.page_kwarg, n=page.next_page_number())
        else:
            next_url = None
        #if previous page is available
        if page.has_previous():
            prev_url = "?{page}={n}".format(
                page=self.page_kwarg, n=page.previous_page_number())
        else:
            prev_url = None
        context = {'startup_list': page,
                   'paginator': paginator,
                   'is_paginated': page.has_other_pages(),
                   'next_page_url':next_url,
                   'previous_page_url': prev_url}
        return render(request, self.template_name, context)


def startup_detail(request, slug):
    context = {'startup': get_object_or_404(Startup, slug__iexact=slug)}
    return render(request, 'organizer/startup_detail.html', context=context)


# def startup_create(request):
#     if request.method == 'POST':
#         form = StartupForm(request.POST)
#         if form.is_valid():
#             new_startup = form.save()
#             return redirect(new_startup)
#         else:
#             return render(request, 'organizer/startup_form.html', {'form':form})
#     else:
#         return render(request, 'orgainzer/startup_form.html', {'form':form})

class StartupCreate(ObjectCreateMixin, View):
    template_name = 'organizer/startup_form.html'
    form_class = StartupForm


class StartupUpdate(ObjectUpdateMixin, View):
    template_name = 'organizer/startup_form_update.html'
    form_class = StartupForm
    model = Startup


class StartupDelete(ObjectDeleteMixin, View):
    template_name = 'organizer/startup_confirm_delete.html'
    model = Startup
    success_url = reverse_lazy('organizer:startup_list')

#views relate to Newslink
class NewslinkCreate(ObjectCreateMixin, View):
    template_name = 'organizer/newslink_form.html'
    form_class = NewslinkForm
            

class NewslinkUpdate(View):
    template_name = 'organizer/newslink_update_form.html'
    form_class = NewslinkForm
    model = Newslink

    def get(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        form = self.form_class(instance=newslink)
        context = {
            'newslink': newslink,
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        form = self.form_class(request.POST, instance=newslink)
        context = {
            'form': form,
            'newslink': newslink
        }
        if form.is_valid():
            updated_link = form.save()
            return redirect(updated_link)
        else:
            return render(request, self.template_name, context)


class NewslinkDelete(View):
    template_name = 'organizer/newslink_confirm_delete.html'
    model = Newslink

    def get(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        return render(request, self.template_name, {'newslink':newslink})
    
    def post(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
