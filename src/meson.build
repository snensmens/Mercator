pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'mercator'
gnome = import('gnome')


blueprints = custom_target('blueprints',
  input: files(
    'ui/window/window.blp',
    'ui/window/setup-quiz-dialog.blp',

    'ui/quiz_overview_page/quiz-overview-page.blp',
    'ui/quiz_overview_page/quiz-entry.blp',

    'ui/quiz_page/quiz-page.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)


gnome.compile_resources('mercator',
  'mercator.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: blueprints,
)


python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'mercator.in',
  output: 'mercator',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr-xr-x'
)

install_data([
  '__init__.py',
  'main.py',
  'quizzes.py'
], install_dir: moduledir)

install_subdir('ui',
  install_dir: moduledir
)

install_subdir('backend',
  install_dir: moduledir
)

install_subdir('maps',
  install_dir: moduledir
)
