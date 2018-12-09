
from rest_framework.renderers import JSONRenderer


class ArticleRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data.pop('code')
            msg = data.pop('msg')
        except:
            code = 200
            msg = '请求成功'
        article_data = {
            'code': code,
            'msg': msg,
            'data': data
        }
        return super().render(article_data, accepted_media_type=None, renderer_context=None)

