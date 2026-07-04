from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkerForm


@login_required
def worker_register(request):

    if request.method == "POST":

        form = WorkerForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            worker = form.save(commit=False)

            worker.user = request.user

            worker.save()

            return redirect("home")

    else:

        form = WorkerForm()

    return render(
        request,
        "workers/register_worker.html",
        {
            "form": form
        }
    )