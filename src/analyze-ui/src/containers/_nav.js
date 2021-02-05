export default [
  {
    _name: 'CSidebarNav',
    _children: [
      {
        _name: 'CSidebarNavItem',
        name: 'Dashboard',
        to: '/dashboard',
        icon: 'cil-speedometer',
        // badge: {
        //   color: 'primary',
        //   text: 'NEW'
        // }
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['Juegos Serios']
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Juegos',
        to: '/games/list',
        icon: 'cil-gamepad'
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Análisis',
        to: '/games/analytics',
        icon: 'cil-chart-line'
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['Configuraciones']
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Descubrimiento',
        to: '/settings/discover',
        icon: 'cil-lightbulb'
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Selección',
        to: '/settings/selection',
        icon: 'cil-highligt'
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Modelado',
        to: '/settings/models',
        icon: 'cil-gem'
      }
    ]
  }
]