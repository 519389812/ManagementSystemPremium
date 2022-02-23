import json
import re
from django.shortcuts import render, reverse, redirect
from bbs.models import Post
from django.core.paginator import Paginator
from ManagementSystemPremium.views import create_related_tree, create_related_list


def bbs(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        post = Post.objects.filter(parent_post__isnull=True)
        paginator = Paginator(post, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'bbs.html', {'page_object_list': list(page.object_list),
                                            'total_num': paginator.count,
                                            'total_page_num': paginator.num_pages,
                                            'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


def view_post(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        comment_post_list = list(Post.objects.filter(parent_post__isnull=False, related_post__iregex=r'\D%s\D' % post_id).values('id', 'content', 'user__full_name', 'submit_datetime', 'parent_post__id'))
        # 将多级结构转成树形结构
        related_post_list = create_related_tree(comment_post_list, post.id, 'parent_post__id', 'id')
        return render(request, 'view_post.html', {'post': post, 'related_post_list': related_post_list})
    else:
        return render(request, 'error_400.html', status=400)


def add_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if re.match(r'^reply\d+:.*', content):
            post_id = re.findall(r'(reply\d+:).*', content)[0].strip('reply:')
        else:
            post_id = request.POST.get('post_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        comment = Post.objects.create(content=content, user=request.user, parent_post=post)
        related_list = json.dumps(create_related_list(comment.id, comment.parent_post))
        comment.related_post = related_list
        comment.save()
        # return redirect(reverse('bbs:view_post', kwargs={'post_id': post_id}))  # 传递url/参数值
        return redirect(reverse('bbs:view_post') + '?%s=%s' % ('post_id', post_id))  # 传递url?参数=参数值
    else:
        return render(request, 'error_400.html', status=400)


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if title == '' or content == '':
            return render(request, 'error_custom.html', {'msg': '提交帖子标题或内容不能为空'})
        post = Post.objects.create(title=title, content=content, user=request.user)
        related_list = json.dumps(create_related_list(post.id, post.parent_post))
        post.related_post = related_list
        post.save()
        return redirect(reverse('bbs:bbs'))
    else:
        return render(request, 'add_post.html')
