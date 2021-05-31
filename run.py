import vfinder


def main():
	app = vfinder.build_app()

	app.run(debug=True, host="0.0.0.0")


if __name__ == '__main__':
	main()
