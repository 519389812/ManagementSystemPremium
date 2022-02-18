import json
import re
from django.shortcuts import render
from bbs.models import Post
from django.core.paginator import Paginator
from ManagementSystemPremium.views import create_related_tree, create_related_list


def bbs(request):
    if request.Method == 'GET':
        page_num = request.GET.get('page', '1')
        post = Post.objects.filter(post=None)
        paginator = Paginator(post, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'bbs.html', {'page_object_list': list(page.object_list),
                                            'total_num': paginator.count,
                                            'total_page_num': paginator.num_pages,
                                            'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


def view_post(request):
    if request.Method == 'GET':
        post_id = request.GET.get('post_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        comment_post_list = list(Post.objects.filter(post__isnull=False, related_post__iregex=r'\D%s\D' % post_id).values('id', 'content', 'user__full_name', 'submit_datetime', 'parent_post__id'))
        # 将多级结构转成树形结构
        related_post_list = create_related_tree(comment_post_list, post_id, 'parent_post__id', 'id')
        return render(request, 'view_post.html', {'post': post, 'related_post_list': related_post_list})
    else:
        return render(request, 'error_400.html', status=400)


def add_comment(request):
    if request.Method == 'POST':
        content = request.POST.get('content', '')
        if re.match(r'^reply\d+:.*', content):
            post_id = re.findall(r'(reply\d+:).*', content)[0].strip('reply:')
        else:
            post_id = request.POST.get('post_id', '')
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(request, 'error_403.html', status=403)
        related_list = json.dumps(create_related_list(post_id, post.parent_post))
        Post.objects.create(content=content, user=request.user, parent_post=post, related_post=related_list)
    else:
        return render(request, 'error_400.html', status=400)


def add_post(request):
    if request.Method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if title == '' or content == '':
            return render(request, 'error_custom.html', {'msg': '提交帖子标题或内容不能为空'})
        post = Post.objects.create(title=title, content=content, user=request.user)
        related_list = json.dumps(create_related_list(post.id, post.parent_post))
        post.update(related_post=related_list)
    else:
        return render(request, 'error_400.html', status=400)