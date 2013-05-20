notification :off
interactor :off

guard :bundler do
  watch('Gemfile')
end

guard 'compass' do
  watch(%r{^scss/(.*)\.s[ac]ss$})
end

guard 'livereload' do
  watch(%r{^static/css/(.*)\.css$})
  watch(%r{^static/js/(.*)\.js$})
  watch(%r{^static/images/(.*)\.(jpg|gif|png)$})
  watch(%r{.+\.(py|html?|php|inc)$})
end

guard 'sprockets', :destination => 'static/js', :asset_paths => ['sjs'], :root_file   => 'sjs/main.js', :minify => false do
  watch(%r{^sjs/.*\.(js|coffee)})
end

guard 'sprockets', :destination => 'static/js', :asset_paths => ['sjs'], :root_file   => 'sjs/preload.js', :minify => false do
  watch(%r{^sjs/.*\.(js|coffee)})
end
