from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Topic, Article


def index(request):
    topics = Topic.objects.all()
    return render(
        request,
        "blog/index.html",
        context={
            "topics": topics,
        }
    )


def topic(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        return Http404("Topic does not exist!")

    return render(
        request,
        "blog/topic.html",
        context={
            "topic": topic,
            "articles": topic.article_set.all(),
        }
    )


def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Http404("Article does not exist!")

    next_article = (
        Article.objects
        .filter(published__gt=article.published)
        .order_by("published")
        .first()
    )

    previous_article = (
        Article.objects
        .filter(published__lt=article.published)
        .order_by("published")
        .last()
    )

    return render(
        request,
        "blog/article.html",
        context={
            "article": article,
            "next": next_article,
            "previous": previous_article,
        }
    )
