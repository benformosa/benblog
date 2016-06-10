% rebase('base.tpl')
<ul>
% for a in articles:
  <li><a href='article/{{a}}'>{{a}}</a></li>
% end
</ul>
